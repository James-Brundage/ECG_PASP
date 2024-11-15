"""
Dataset utils for working with UCSF data. Developed by JNB. 
james.brundage@ucsf.edu
james.brundage@hsc.utah.edu
james.n.brundage@gmail.com
jamesnick.brundage@gmail.com
"""

# Imports (Try to keep minimum imports)
import os
import pandas as pd
import numpy as np
import torch
    
from scipy import signal
def load_ecg_freq (ecg_path, freq=5000):
    ecg_raw = np.loadtxt(ecg_path, skiprows=1, delimiter=',', usecols=range(12))
    timepoints, leads = ecg_raw.shape
    if timepoints != freq:
        return signal.resample(ecg_raw, freq)
    else:
        return ecg_raw
    
def load_ecg (ecg_path, freq=5000):
    ecg_raw = np.load(ecg_path)
    ecg_raw = ecg_raw.T
    timepoints, leads = ecg_raw.shape
    if timepoints != freq:
        return signal.resample(ecg_raw, freq)
    else:
        return ecg_raw

    
# Define a function named get_scale that takes two arguments: scale_dir and scale_key
def get_scale_from_file (scale_dir, scale_key):
    # List all files in the scale_dir that contain the specified scale_key
    files = [f for f in os.listdir(scale_dir) if scale_key in f]
    
    # Filter files that contain 'mean' in their name
    mean_file = [f for f in files if 'mean' in f]
    
    # Filter files that contain 'std' in their name
    std_file = [f for f in files if 'std' in f]
    
    # Ensure that there is exactly one mean file and one std file
    assert len(mean_file) == 1
    assert len(std_file) == 1
    
    # Create the full paths to the mean and std files using os.path.join
    mean_pth = os.path.join(scale_dir, mean_file[0])
    std_pth = os.path.join(scale_dir, std_file[0])
    
    # Open the mean file in binary read mode and load its contents into the 'means' variable using NumPy
    with open(mean_pth, 'rb') as f:
        means = np.load(f)
    
    # Open the std file in binary read mode and load its contents into the 'stds' variable using NumPy
    with open(std_pth, 'rb') as f:
        stds = np.load(f)
    
    # Return the 'means' and 'stds' as a tuple
    return means, stds

# Negative 1 to 1 scaler
def neg_one_to_one (x):
    return (2*(x-np.min(x))/(np.max(x) - np.min(x)))-1

# Utah ECG Dataset
class InfDataset (torch.utils.data.Dataset):
    
    def __init__(self,
        dataset_paths_list,
        scale_dir,
        x_transforms,
        scale_to_self):
        

        self.dataset_paths_list = dataset_paths_list
        self.x_transforms = x_transforms
        self.scale_to_self=scale_to_self
        
    def __len__(self):
        return len(self.dataset_paths_list)
        
    def __getitem__(self, idx):
        
        # Grab filepath from manifest
        filepath = self.dataset_paths_list[idx]
        
        # Load ECG
        ecg = load_ecg(filepath)
        
        # Scaling to self 
        if self.scale_to_self:
            ecg = neg_one_to_one(ecg)
        
        # Perform transforms
        if self.x_transforms:
            ecg = np.transpose(ecg)
            ecg = self.x_transforms(ecg)
            ecg = np.transpose(ecg)
            
        # To tensor
        ecg = torch.tensor(ecg, dtype=torch.float32)
        
        # Add channel for Utah format
#         ecg = ecg.unsqueeze(0)
        
        return ecg, 1