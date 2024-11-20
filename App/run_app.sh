EXTRACT="$1"
INFERENCE="$2"

git clone https://github.com/James-Brundage/ECG_PASP.git
cd ECG_PASP/

git-lfs install
git lfs fetch
git lfs checkout

# Extraction step
if [ "${EXTRACT}" = "TRUE" ]; then
    python App/XML_Extraction/Extraction.py
fi

# Inference
if [ "${INFERENCE}" = "TRUE" ]; then
    chmod +x App/XML_Extraction/xml2ecg_updatedleads.linux
    python App/Model_Inference/apply.py
fi