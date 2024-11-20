# Create sample dirs for example
mkdir Extraction_out
mkdir Preds_Out

# Define args
XML_DIR="$(pwd)"/Sample_Data_Source
EXTRACTION_OUTPUT_DIR="$(pwd)"/Extraction_out
PREDS_OUTPUT_DIR="$(pwd)"/Preds_Out
IMAGE_NAME=ecg_pasp_v2
IMAGE_TAG=latest
EXTRACT="TRUE"
INFERENCE="TRUE"

# Check requirements
check_docker_installed() {
    if command -v docker &> /dev/null; then
        return 0
    else
        return 1
    fi
}

check_docker_installed
status=$?  # Store the exit status
if [[ $status -eq 0 ]]; then
    echo "Docker confirmed."
else
    echo "Docker not isntalled, please install and try again."
    exit 1
fi


# Check if docker image exists, build if it doesn't
if docker image inspect "${IMAGE_NAME}:${IMAGE_TAG}" > /dev/null 2>&1; then
    echo "Docker image ${IMAGE_NAME}:${IMAGE_TAG} exists."
else
    echo "Docker image ${IMAGE_NAME}:${IMAGE_TAG} not yet built, building..."
    # Optionally, you can pull or build the image here
    # pwd
    docker build -f "$(pwd)"/App/Dockerfile -t $IMAGE_NAME "$(pwd)"/App/
fi

# Docker run command
docker run -it --rm \
--mount type=bind,source=$XML_DIR,target=/Data_Source \
--mount type=bind,source=$EXTRACTION_OUTPUT_DIR,target=/extraction_output \
--mount type=bind,source=$PREDS_OUTPUT_DIR,target=/Preds_output \
--mount type=bind,source="$(pwd)"/App,target=/AppStarter \
--name pasp_container \
"${IMAGE_NAME}:${IMAGE_TAG}" bash /AppStarter/run_app.sh $EXTRACT $INFERENCE