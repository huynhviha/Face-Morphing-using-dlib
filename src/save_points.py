import numpy as np
import dlib
import cv2
import sys


def save_points(im, im_path, rects):
	path = "shape_predictor_68_face_landmarks.dat"
	predict = dlib.shape_predictor(path)
	landmark = predict(im, rects[0])
	save_path = im_path.replace(".jpg", ".txt")
	file = open(save_path, "w+")
	for idx, point in enumerate(landmark.parts()):
		if idx >= 48:
			s = str(point.x) + " " + str(point.y) + "\n"
			file.write(s)
			
if __name__ == '__main__':
	detector = dlib.get_frontal_face_detector()
	im_path = sys.argv[1]
	im = cv2.imread(im_path)
	rects = detector(im,1)
	save_points(im, im_path, rects)
	
	

			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			