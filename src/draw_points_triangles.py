import numpy as np
import dlib
import cv2
import sys

def rect_contains(rect, point) :
    if point[0] < rect[0] :
        return False
    elif point[1] < rect[1] :
        return False
    elif point[0] > rect[2] :
        return False
    elif point[1] > rect[3] :
        return False
    return True

def draw_point(im, p, color):
    cv2.circle(im,p, 2,color ,1)
            
def draw_delaunay(img, subdiv, delaunay_color) :
    triangleList = subdiv.getTriangleList()
    size = img.shape
    r = (0, 0, size[1], size[0])
    for t in triangleList :
        
        pt1 = (t[0], t[1])
        pt2 = (t[2], t[3])
        pt3 = (t[4], t[5])
         
        if rect_contains(r, pt1) and rect_contains(r, pt2) and rect_contains(r, pt3) :
         
            cv2.line(img, pt1, pt2, delaunay_color, 1)
            cv2.line(img, pt2, pt3, delaunay_color, 1)
            cv2.line(img, pt3, pt1, delaunay_color, 1)
			
def get_id(subdiv):
	leadingedgeList = subdiv.getLeadingEdgeList()
	print (leadingedgeList)
			
def load_point(im_path):
	points = []
	save_points_path = im_path.replace(".jpg", ".txt")
	with open(save_points_path) as file:
		for line in file:
			x, y = line.split()
			x = int(x)
			y = int(y)
			points.append((x, y))
	return points
	
def get_subdiv(points, rect):
	subdiv = cv2.Subdiv2D(rect)
	for p in points:
		subdiv.insert(p)
	return subdiv
	
def draw_points(im, points):
	for p in points:
		draw_point(im, p, (0, 255, 0))

if __name__ == "__main__":
	detector = dlib.get_frontal_face_detector()
	im_path = sys.argv[1]
	im = cv2.imread(im_path)
	rects = detector(im,1)
	size = im.shape
	rect = (0, 0, size[1], size[0])
	
	points = load_point(im_path)
	draw_points(im, points)
	subdiv = get_subdiv(points, rect)
	draw_delaunay(im, subdiv, (255, 255, 255))
	get_id(subdiv)
	
	cv2.imshow("im",im)
	cv2.waitKey()
	cv2.destroyAllWindows()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	