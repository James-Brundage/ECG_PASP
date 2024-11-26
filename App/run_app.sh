EXTRACT="$1"
INFERENCE="$2"
WEIGHTS_NAME="$3"

# Extraction step
if [ "${EXTRACT}" = "TRUE" ]; then
    chmod +x /AppStarter/XML_Extraction/xml2ecg_updatedleads.linux
    python /AppStarter/XML_Extraction/Extraction.py
fi

# Inference
if [ "${INFERENCE}" = "TRUE" ]; then
    python /AppStarter/Model_Inference/apply.py $3
fi