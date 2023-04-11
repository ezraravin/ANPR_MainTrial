# %%
import cv2
import numpy as np
import os
from sklearn import tree
from Module01_YOLO import *
from Module02_TextRecognition import *
from imutils.object_detection import non_max_suppression

# %%
# settings
imgROI_FileName = "./roi/roi123.jpg"

# %%
# LOAD YOLO MODEL (OBJECT DETECTION)
# LOAD EAST MODEL (CHARACTER SEGMENTATION)
# LOAD CRNN MODEL (CHARACTER DECODING)
modelYOLO = funcLoadYOLOModel('./Model/weights/best.onnx')
modelEAST = cv2.dnn.readNet('./frozen_east_text_detection.pb')
modelCRNN = cv2.dnn.readNet('./crnn.onnx')

# %%
# predictions
def yolo_predictions(img, modelYOLO):
    # step-1: detections
    input_image, detections = get_detections(img, modelYOLO)
    # step-2: NMS
    boxes_np, confidences_np, index = non_maximum_supression(input_image, detections)
    # step-3: Region Of Interest Extraction + Draw ROI
    result_img = funcExtractRegionOfInterest(img, boxes_np, confidences_np, index, imgROI_FileName)
    # step-4 : Text Segmentation & Extraction Combo
    text = funcExtractText(imgROI_FileName, modelEAST, modelCRNN)
    return result_img, text

import tkinter as tk
import ttkbootstrap as ttk
from PIL import ImageTk, Image

window = ttk.Window()
window.title('Automatic Number Plate Recognizer System')
window.geometry('1000x1000')
# Create a label in the window for video
videoStreamFrame = tk.Label(master=window)

# Label for photo streaming
photoStreamFrame = tk.Label(master=window)

# Create label for Number Plate Display
labelNumberPlate = ttk.Label(master=window, text="Number Plate", font='Roboto 100 bold')

# Pack and show widgets
videoStreamFrame.pack(pady=20)
labelNumberPlate.pack(pady=10, padx=10)
photoStreamFrame.pack(pady=20)


# Capture from camera
cap = cv2.VideoCapture(0)

# function for video streaming
def video_stream():
    ret, frame = cap.read()
    
    results, text = yolo_predictions(frame, modelYOLO)
    labelNumberPlate['text'] = text

    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    videoStreamFrame.imgtk = imgtk
    videoStreamFrame.configure(image=imgtk)
    imgROI_GUI = Image.open(imgROI_FileName)
    imgROI_GUI_tk = ImageTk.PhotoImage(imgROI_GUI)
    photoStreamFrame.imgtk = imgROI_GUI_tk
    photoStreamFrame.configure(image=imgROI_GUI_tk)
    photoStreamFrame.after(1, video_stream)


video_stream()
# photo_stream()

# Loop
window.mainloop()