#!/usr/bin/python3

import sys
print((sys.version))

if sys.version_info[0] < 3:
    print("This script requires Python version 3.x")
    sys.exit(1)

import glob
import os


class Core():

    def __init__(self, ctrl):
        super(Core, self).__init__()
        self.ctrl = ctrl

        self.path_txt = ""

        print("core")

    def setPath(self, path):
        self.path_txt = path
        self.showFiles(path)

    def showFiles(self, path):
        imagesList = glob.glob(path + os.pathsep + '*.jpg')
        print(imagesList)
        for img in imagesList:
            print(img)