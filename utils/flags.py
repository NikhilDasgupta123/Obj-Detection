import cv2
from config.config import Config
import numpy as np


new_count = 0

# About Object Information
def flagsDetected(results):
    for result in results:
      boxes = result.boxes  # Boxes object for bbox outputs
      cls = boxes.cls.tolist()  # Convert tensor to list
      # print(cls) # Class Index Array
      
      
      global new_arr
      new_arr = []
      for class_index in cls:
            if class_index == 4.0 or class_index==5.0 or class_index==6.0:
                new_arr.append(class_index)
    

      print(new_arr)
      flags = 0
      for i in new_arr:
            if i == 5.0 or i==4.0 or i==6.0:
                flags += 1


      # Putting Value in dict Flags
      text_info={
          'FLAGS' : flags
      }

      global Flags
      Flags = flags
      print('Total: ',Flags)
      

      return text_info




# Putting Text Flags
def puttext(annotated_frame,text_info):

    # Display the text upside down at the bottom of the frame
    text_y = annotated_frame.shape[0] - 190  # Starting position at the bottom of the frame
    
    # display the Text
    for i, (key, value) in enumerate(text_info.items()):
        reversed_text = key + ': ' + str(value)
        text_size = cv2.getTextSize(reversed_text, Config.font, Config.font_scale, Config.font_thickness)[0]
        text_x = 10  # Center the text horizontally
        # Draw white rectangle as background
        text_coords = ((text_x, text_y - text_size[1]), (text_x + text_size[0], text_y))

        background_coords = ((text_coords[0][0] - Config.padding, text_coords[0][1] - Config.padding),
                     (text_coords[1][0] + Config.padding, text_coords[1][1] + Config.padding))

        # Draw text on top of the white rectangle
        cv2.rectangle(annotated_frame, background_coords[0], background_coords[1], Config.background_color, -1)
        cv2.putText(annotated_frame, reversed_text, (text_x, text_y), Config.font, Config.font_scale, Config.text_color, Config.font_thickness)


        text_y -= text_size[1] + 10  # Adjust the y-position for the next line







