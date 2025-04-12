import os
import sys
import torch

# Fix for PosixPath issue on Windows
import pathlib
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

# Command to run the detector
command = 'python detect.py --weights best.pt --source 0 --conf 0.5 --view-img'

# Run the command
os.system(command)