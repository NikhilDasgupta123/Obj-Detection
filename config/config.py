import cv2
from ultralytics import YOLO  # YOLO model

# Config 
class Config:
    DEGUG =True 
    weight = 'WEIGHT/model_last(9).pt'                    # last weight
    model = YOLO(weight)                            # YOLO model
    video_path = "Video/new5.mp4"
    cap = cv2.VideoCapture(video_path)        #demo video
    

    # Frame Text
     # Define the font parameters
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.7  # Reduced font size
    text_color = (255, 0, 0)  # Black text color
    background_color = (255, 255, 255)  # White background color
    font_thickness = 2
    padding = 5
    text_color_red = (0, 0, 255) # Red Text color

