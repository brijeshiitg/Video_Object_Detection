import cv2
import numpy as np
import os
from arguments import Args
opt = Args()

# set video file path of input video with name and extension
# video_file_path='./video/'
# file_name = 'msh.mp4'
vid = cv2.VideoCapture(opt.video_path+opt.file_name)


if not os.path.exists(opt.video_path+'video_frames_'+opt.file_name.split('.')[0]):
    os.makedirs(opt.video_path+'video_frames_'+opt.file_name.split('.')[0])

#for frame identity
index = 0
while(True):
    # Extract images
    ret, frame = vid.read()
    # end of frames
    if not ret: 
        break
    # Saves images
    name = opt.video_path+'video_frames_'+opt.file_name.split('.')[0]+'/'+ str(index) + '.jpg'
    print ('Creating...' + name)
    cv2.imwrite(name, frame)

    # next frame
    index += 1