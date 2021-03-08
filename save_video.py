import cv2
import numpy as np
import os
from arguments import Args
opt = Args()

def frames_to_video(inputpath,outputpath,fps):
   image_array = []
   files = [f for f in os.listdir(inputpath) if os.path.isfile(os.path.join(inputpath, f))]
   files.sort(key = lambda x: int(x.split(".")[0]))
   # files.sort()
   # print(files)
   for i in range(len(files)):
       img = cv2.imread(os.path.join(inputpath, files[i]))
       size =  (img.shape[1],img.shape[0])
       img = cv2.resize(img,size)
       image_array.append(img)
   fourcc = cv2.VideoWriter_fourcc('D', 'I', 'V', 'X')
   out = cv2.VideoWriter(outputpath,fourcc, fps, size)
   for i in range(len(image_array)):
       out.write(image_array[i])
   out.release()


inputpath = opt.video_path+'detected_frames_'+opt.file_name.split('.')[0]#'./video/video_frames/_detections'
outpath =  opt.video_path+'detected_'+opt.file_name
fps = 29
frames_to_video(inputpath,outpath,fps)