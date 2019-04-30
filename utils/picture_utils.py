# coding:utf-8
import cv2 as cv
import os
import sys

__all__ = ['PictureUtil']


class PictureUtil(object):

    def __init__(self):
        pass

    @staticmethod
    def get_picture_part(image, coordinate):
        return image[coordinate['y1']: coordinate['y2'], coordinate['x1']: coordinate['x2']]

    @staticmethod
    def show_pic(load_path, name):
        image = cv.imread(load_path + name)
        cv.imshow("Image", image)
        cv.waitKey(0)