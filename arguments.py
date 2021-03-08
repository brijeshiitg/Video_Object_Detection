import argparse

def Args():
	parser = argparse.ArgumentParser()
	parser.add_argument('--file_name', default='msh.mp4')
	parser.add_argument('--video_path', default='./video/')
	# parser.add_argument('--frame_path', default='video_frames/')

	opt = parser.parse_args()
	return opt
