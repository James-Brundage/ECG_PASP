import os
import subprocess
import stat
import tqdm

# Set dirs
data_source_dir='/Data_Source'
extraction_output_dir='/extraction_output/'

# Reset working dir to where this file is located
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# # Ensure linux file can be run
# st = os.stat('xml2ecg_updatedleads.linux')
# os.chmod('xml2ecg_updatedleads.linux', st.st_mode | stat.S_IEXEC)

# Directory with xml files
xml_file_dir = '/Data_Source'

# Create paths to files 
files = os.listdir(xml_file_dir)
paths = [os.path.join(xml_file_dir, f) for f in files if '.xml' in f]
keys = [s.split('.xml')[0].split('/')[-1] for s in paths]

# Perform Extraction to same folder as script
for i in tqdm.tqdm(range(len(paths))):

    # Extract individual xml
    p = paths[i]
    command = './xml2ecg_updatedleads.linux --muse {}'.format(p)
    command = command.split(' ')
    subprocess.run(command)

    # Copy to target file
    k = keys[i]
    command2 = 'cp {}_full.npy {}'.format(k, extraction_output_dir)
    command2 = command2.split(' ')
    subprocess.run(command2)
