import torch 
from torch.utils.data import DataLoader
import os
from Dataloading import InfDataset
import tqdm
import pandas as pd

# Reset working dir to where this file is located
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# Check device 
device = torch.device("cpu")
if torch.cuda.is_available():
    device = torch.device("cuda")

# JIT Model
model_path = '1xy5agl8_Jit_PASP_TRVmax_JPE_705386.pth'
net = torch.jit.load(f'{model_path}', map_location=device)
net.to(device)
_ = net.eval()

# Load data (sample)
sample_data_path = '/extraction_output/'
paths = [os.path.join(sample_data_path, f) for f in os.listdir(sample_data_path) if '_full.npy' in f]

# Set up inference dataset
dataset = InfDataset(
        dataset_paths_list=paths,
        scale_dir=False,
        x_transforms=None,
        scale_to_self=False)

dataloader = DataLoader(dataset, 
                                batch_size=1, 
                                shuffle=False,  
                                drop_last=False)

# Perform inference
preds = []
for i, data in enumerate(tqdm.tqdm(dataloader, leave=False)):

    x, y = data
    predicted_pasp = net(x)
    preds.append(predicted_pasp.item())

# Get file name
names=[p.split('/')[-1].split('_full.npy')[0] for p in paths]

# Create output df
out_df = pd.DataFrame({
    'File':names,
    'Predicted_PASP':preds
})

# Generate csv
out_df.to_csv('/Preds_output/Predicted_PASP_Results.csv', index=False)