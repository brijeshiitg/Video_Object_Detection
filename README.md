# Video_Object_Detection

## Demo

  <img src="https://user-images.githubusercontent.com/21377671/110315178-e55f2180-802e-11eb-9569-684a6220100a.gif" width="500" height="400"> 
  <img src="https://user-images.githubusercontent.com/21377671/110324824-86080e00-803c-11eb-9921-f6e38937545d.gif" width="500" height="400">


 ## Setup
 1. Setup your environment by installing "requirement.txt"

 2. Download pretrined weights of YOLOv3 and place into 'config' directory

 3. Pretrained weights are available at:[YOLOv3 weights](https://drive.google.com/file/d/1GsEvAXcgzpKIZnB3raYngbz126dLkXr8/view?usp=sharing)

 4. Place your test video in 'video' directory

 5. modify 'arguments.py' file by giving name of the video file

 6. run the script "run_video_object_detection.sh"

 7. Output: This code first converts the given video 
 	to sequence of frame then applies detection on individual frames. Later detected
 	frames are transformed to video.
 	Therefore, it generates two intermediate directories (1) to keep converted video frames
 	and (2) to keep detected frames

 8. The final output will be 'detected_filename'


Credit: Some of code snippets have been taken from [repo](https://github.com/cfotache/pytorch_objectdetecttrack?fbclid=IwAR0Ih6PoswYW_JptXRWMJ6LX2hcKr82ROvOlYwPLE04RjreyCXsxVyv2XQk)
