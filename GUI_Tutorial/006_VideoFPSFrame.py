from tkinter import *
import imageio
from PIL import Image, ImageTk
# import cv2

# cap = cv2.VideoCapture(0)

def stream():
    try:
        # _, frame = cap.read()
        image = video.get_next_data()
        frame_image = Image.fromarray(image)
        frame_image=ImageTk.PhotoImage(frame_image)
        l1.config(image=frame_image)
        l1.image = frame_image
        l1.after(delay, lambda: stream())
    except:
        video.close()
        return   
########### Main Program ############
root = Tk()
root.title('Video in a Frame')
f1=Frame()
l1 = Label(f1)
l1.pack()
f1.pack()
video_name = "Futurama.mkv"   #Image-path
video = imageio.get_reader(0)
delay = int(1000 / video.get_meta_data()['fps'])
stream()
root.mainloop()