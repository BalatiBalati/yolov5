# Save this as convert_model.py
import torch
import pathlib

# Patch PosixPath for Windows
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

# If you have best.pt, convert it:
try:
    print("Attempting to convert your model...")
    model = torch.load('best2.pt', map_location='cpu')
    torch.save(model, 'best_windows2.pt')
    print("Model converted successfully to best_windows.pt")
except FileNotFoundError:
    print("best.pt not found, downloading pre-trained model instead...")
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
    torch.save(model, 'yolov5s_windows.pt')
    print("Downloaded and saved pre-trained model as yolov5s_windows.pt")