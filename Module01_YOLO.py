import numpy as np
import cv2
from ModuleGlobal import *

# LOAD YOLO MODEL
def funcLoadYOLOModel(paramFilePath):
    net = cv2.dnn.readNetFromONNX(paramFilePath)
    net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
    net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)
    return net

# CONVERT IMAGE TO YOLO FORMAT
def funcConvertImageToYOLO(paramImage):
    inputImage = paramImage.copy()
    row, col, d = inputImage.shape

    max_rc = max(row, col)
    YOLO_FormatImage = np.zeros((max_rc, max_rc, 3), dtype=np.uint8)
    YOLO_FormatImage[0: row, 0: col] = inputImage
    return YOLO_FormatImage


def funcPredictFromYOLO(paramYOLO_FormatImage, paramNeuralNetwork, paramInputWidth, paramInputHeight):
    blob = cv2.dnn.blobFromImage(
        paramYOLO_FormatImage, 1/255, (paramInputWidth, paramInputHeight), swapRB=True, crop=False)
    paramNeuralNetwork.setInput(blob)
    predicitionsArray = paramNeuralNetwork.forward()
    detections = predicitionsArray[0]
    return detections

# STEP 1 : GET OBJECT DETECTIONS
def get_detections(paramInputImage, paramNeuralNetwork):
    # CONVERT IMAGE TO YOLO FORMAT
    YOLO_FormatImage = funcConvertImageToYOLO(paramInputImage)

    # GET PREDICTION FROM YOLO MODEL
    detections = funcPredictFromYOLO(
        YOLO_FormatImage, paramNeuralNetwork, INPUT_WIDTH, INPUT_HEIGHT)

    return YOLO_FormatImage, detections

# STEP 2 : FILTER DOWN THE OBJECT DETECTIONS TO THE BEST ONE
def non_maximum_supression(input_image, detections):
    # FILTER DETECTIONS BASED ON CONFIDENCE AND PROBABILIY SCORE
    # center x, center y, w , h, conf, proba
    boxes = []
    confidences = []

    image_w, image_h = input_image.shape[:2]
    x_factor = image_w/INPUT_WIDTH
    y_factor = image_h/INPUT_HEIGHT

    for i in range(len(detections)):
        row = detections[i]
        confidence = row[4]  # confidence of detecting license plate
        if confidence > 0.4:
            class_score = row[5]  # probability score of license plate
            if class_score > 0.25:
                cx, cy, w, h = row[0:4]

                left = int((cx - 0.5*w)*x_factor)
                top = int((cy-0.5*h)*y_factor)
                width = int(w*x_factor)
                height = int(h*y_factor)
                box = np.array([left, top, width, height])

                confidences.append(confidence)
                boxes.append(box)
    # clean
    boxes_np = np.array(boxes).tolist()
    confidences_np = np.array(confidences).tolist()
    # NMS
    index = np.array(cv2.dnn.NMSBoxes(
        boxes_np, confidences_np, 0.25, 0.45)).flatten()
    return boxes_np, confidences_np, index
