#!/usr/bin/python3

import sys
print((sys.version))

if sys.version_info[0] < 3:
    print("This script requires Python version 3.x")
    sys.exit(1)

from mgncc_core import Core
from mgncc_ui import Ui


class Controller():

    def __init__(self):
        super(Controller, self).__init__()
        print("controller")
        self.mgncc = Core(self)
        self.ui = Ui(self)

###########################
# Launch app
###########################
ctrl = Controller()