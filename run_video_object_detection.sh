#! /bin/bash

echo "converting video to image frames:"

python get_frames.py

echo "video converted to frames. Now running detection:"

python test.py

echo "all frames have been processed. Making video now..."
python save_video.py


echo "done!!"


