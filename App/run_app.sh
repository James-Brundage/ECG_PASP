EXTRACT="$1"
INFERENCE="$2"

# Extraction step
if [ "${EXTRACT}" = "TRUE" ]; then
    python /App/XML_Extraction/Extraction.py
fi

# Inference
if [ "${INFERENCE}" = "TRUE" ]; then
    python /App/Model_Inference/apply.py
fi