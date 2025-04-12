import os
import sys
import pathlib

# Fix for PosixPath issue on Windows
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

# Command to run the detector with original YOLOv5 detect.py
model_path = 'best_windows2.pt' if os.path.exists('best_windows2.pt') else 'yolov5s.pt'
print(f"Using model: {model_path}")

# Use a lower confidence threshold to try to detect more signs
command = f'python detect.py --weights {model_path} --source 0 --conf 0.81 --view-img'
print(f"Running: {command}")

# Run the command
os.system(command)