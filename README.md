

# Video_Object_Detection

#Demo#

![detected_msh](https://user-images.githubusercontent.com/21377671/110313967-3c63f700-802d-11eb-8862-9e7f1ca76e40.gif)
 
 1. Setup your environment by installing "requirement.txt"

 2. Download pretrined weights of YOLOv3 and place into 'config' directory

 3. Pretrained weights are available at:[[YOLOv3 weights](https://drive.google.com/file/d/1GsEvAXcgzpKIZnB3raYngbz126dLkXr8/view?usp=sharing)]

 4. Place your test video in 'video' directory

 5. modify 'arguments.py' file by giving name of the video file

 6. run the script "run_video_object_detection.sh"

 7. Output: This code first converts the given video 
 	to sequence of frame then applies detection on individual frames. Later detected
 	frames are transformed to video.
 	Therefore, it generates two intermediate directories (1) to keep converted frames
 	and (2) to keep detected frames

 8. The final output will be 'detected_filename'
