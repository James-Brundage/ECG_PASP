# ECG-PASP Validation Pipeline

## Overview
This repo set up to build the appropriate docker image and run a docker container that can extract .XML ECG files to .npy files in the same format that were used for training, then perform model inference with a model JIT.

## Install 
The inference/extraction runs on a docker container. It assumes that it is running on a linux OS. Git and docker are required. All other requirements install as part of the docker container and do not need to be locally installed.

1) Install git and docker
2) Clone this repo
3) Download model JIT
4) In example.sh, change the WEIGHTS_DIR to the directory where the model JIT is stored and change WEIGHTS_NAME to the name of the downloaded JIT.
5) Run example.sh, which will run extraction and inference on example ECGs stored in the repo. 
6) Change target directories listed below to meet preference, and then run on run.sh for final inference

## Setup And Running Inference

To use the repo, first clone the repo to your device. Then open the run.sh script. You will need to specify a few directories. Please set the following: 

1) XML_DIR - The absolute path to the directory where the target XMLs are stored 
2) EXTRACTION_OUTPUT_DIR - The absolute path to the directory where the .npy files will be extracted to. 
3) PREDS_OUTPUT_DIR - The absolute path to the directory where the .csv containing the model predictions will go. 
4) WEIGHTS_DIR and WEIGHTS_NAME are described above. 

The image name and tag do not need to be changed. 

If you set EXTRACT=TRUE, the script will extract the XML files to the target directoy. If it is set to anything else, it will not. Similarly, if you set INFERENCE=TRUE, the script will run inference on extracted .npy files in the extraction target directory. If it is set to antything else, it will not. 

There is also a separate script, example.sh, that demonstrates how this mapping can work and creates example folders, and run the code on sample data included. 