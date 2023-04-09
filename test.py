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
from tkinter import *
from PIL import ImageTk, Image

root = tk.Tk()
root.title('Automatic Number Plate Recognizer System')
root.geometry('1000x1000')
# Create a frame
app = Frame(root, bg="white")
app.pack(pady=10)
# Create a label in the frame
lmain = Label(app)
lmain.pack()
# Create another frame
frameNumberPlate = Frame(root, bg="white")
frameNumberPlate.pack()
labelNumberPlate = Label(frameNumberPlate, text="Number Plate", font='Calibri 24 bold')
labelNumberPlate.pack(pady=10, padx=10)

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
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(1, video_stream)

video_stream()

# Loop
root.mainloop()