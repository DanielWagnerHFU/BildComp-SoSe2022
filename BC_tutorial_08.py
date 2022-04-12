import numpy as np
import cv2
from math import *

class DrawLineWidget(object):
    def __init__(self):
        self.imageOriginal = cv2.resize(cv2.imread('images/IMG_3232.JPEG'), dsize=(0,0), fx=0.4, fy=0.4)
        self.imageClone = self.imageOriginal.copy()
        cv2.namedWindow('image')
        cv2.setMouseCallback('image', self.extract_coordinates)
        self.image_coordinates = []
        self.line_coordinates = []

    def extract_coordinates(self, event, x, y, flags, parameters):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.image_coordinates = [(x,y)]
        elif event == cv2.EVENT_LBUTTONUP:
            self.image_coordinates.append((x,y))
            cv2.line(self.imageClone, self.image_coordinates[0], self.image_coordinates[1], (36,255,12), 2)
            self.line_coordinates.append(self.image_coordinates)
            cv2.imshow("image", self.imageClone)
        elif event == cv2.EVENT_RBUTTONDOWN:
            self.imageClone = self.imageOriginal.copy()

    def getImage(self):
        return self.imageClone

    def getLines(self):
        return self.line_coordinates

if __name__ == '__main__':
    draw_line_widget = DrawLineWidget()
    while True:
        cv2.imshow('image', draw_line_widget.getImage())
        cv2.waitKey(1)
        if len(draw_line_widget.getLines()) == 2:
            break
    lines = draw_line_widget.getLines()

    print(lines)
    A1 = np.array([lines[0][0][0],lines[0][0][1],1])
    B1 = np.array([lines[0][1][0],lines[0][1][1],1])
    A2 = np.array([lines[1][0][0],lines[1][0][1],1])
    B2 = np.array([lines[1][1][0],lines[1][1][1],1])
    point = np.cross(np.cross(A1, B1), np.cross(A2, B2))
    point = point / point[2]
