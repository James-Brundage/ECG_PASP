EXTRACT="$1"
INFERENCE="$2"

# pip install --no-cache-dir -r requirements.txt

# Extraction step
if [ "${EXTRACT}" = "TRUE" ]; then
    python /App/XML_Extraction/Extraction.py
fi

# Inference
if [ "${INFERENCE}" = "TRUE" ]; then
    chmod +x /App/XML_Extraction/xml2ecg_updatedleads.linux
    python /App/Model_Inference/apply.py
fi