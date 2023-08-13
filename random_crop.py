import cv2
import os
import numpy as np

# video_path = r"C:\Users\USERROR\Downloads\video1_cut.mp4"
# output_directory = r"C:\Users\USERROR\Desktop\4.2\Project\out"

video_capture = cv2.VideoCapture(video_path)

# min_dimension = float('inf')
frame_interval = 1
frame_counter = 0

while True:
    ret, frame = video_capture.read()
    if not ret:
        break

    # Get the dimensions of the current frame
    height, width = frame.shape[:2]

    # Update the minimum frame dimension
    min_dimension = min(height, width)

    # Perform random crop on the resized frame
    crop_size = (min_dimension // 2, min_dimension // 2)
    y = np.random.randint(0, min_dimension - crop_size[0])
    x = np.random.randint(0, min_dimension - crop_size[1])
    cropped_frame = frame[y:y + crop_size[0], x:x + crop_size[1]]

    frame_filename = os.path.join(output_directory, f"frame_{frame_counter}.jpg")
    cv2.imwrite(frame_filename, cropped_frame)
    
    frame_counter += 1

# Release the video capture
video_capture.release()
