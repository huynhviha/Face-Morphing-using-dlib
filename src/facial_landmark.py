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

def draw_point(im, point, color):
    cv2.circle(im,(point.x,point.y),2,color ,1)
            
def draw_delaunay(img, subdiv, delaunay_color) :
 
    triangleList = subdiv.getTriangleList();
    size = img.shape
    r = (0, 0, size[1], size[0])
    print(triangleList)
    for t in triangleList :
        
        pt1 = (t[0], t[1])
        pt2 = (t[2], t[3])
        pt3 = (t[4], t[5])
         
        if rect_contains(r, pt1) and rect_contains(r, pt2) and rect_contains(r, pt3) :
         
            cv2.line(img, pt1, pt2, delaunay_color, 1)
            cv2.line(img, pt2, pt3, delaunay_color, 1)
            cv2.line(img, pt3, pt1, delaunay_color, 1)
#create object detection
detector = dlib.get_frontal_face_detector()
# load image
im_path = sys.argv[1]
im = cv2.imread(im_path)
rects = detector(im,1)
size = im.shape
rect = (0, 0, size[1], size[0])
# xem kết quả
for d in rects:
    cv2.rectangle(im,(d.left(),d.top()),(d.right(),d.bottom()),(0,255,0),2)

path = "shape_predictor_68_face_landmarks.dat"
predict = dlib.shape_predictor(path)
landmark = predict(im, rects[0])
points = []
file = open(im_path + ".txt", "w+")
for idx, point in enumerate(landmark.parts()):
    if idx >= 48:
        points.append((point.x, point.y))
        draw_point(im, point, (0, 255, 0))
        s = str(point.x) + " " + str(point.y) + "\n"
        file.write(s)
subdiv = cv2.Subdiv2D(rect)
for p in points:
    subdiv.insert(p)
draw_delaunay(im, subdiv, (255, 255, 255))

cv2.imshow("im",im)
cv2.waitKey()
cv2.destroyAllWindows()
