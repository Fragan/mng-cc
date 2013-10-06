#!/usr/bin/python3

import sys
print((sys.version))

if sys.version_info[0] < 3:
    print("This script requires Python version 3.x")
    sys.exit(1)

import tkinter.filedialog as fd
from mgncc_core import Core
from mgncc_ui import Ui


class Controller():

    def __init__(self):
        super(Controller, self).__init__()
        print("controller")
        self.abstraction = Core(self)
        self.presentation = Ui(self)
        self.presentation.setPath("trololo")

    def p2c_browse(self):
        print("ctrl.browse()")
        path = fd.askdirectory(title="Select a directory")
        self.abstraction.setPath(path)
        #self.presentation.setPath(path) Error: 'Controller' object has no attribut 'presentation'

    def p2c_next(self):
        print("ctrl.next()")

    def p2c_previous(self):
        print("ctrl.previous()")

    def c2p_dispay_picture(self, img_path):
        self.ui.dispay_picture(img_path)

###########################
# Launch app
###########################
ctrl = Controller()