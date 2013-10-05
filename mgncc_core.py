#!/usr/bin/python3

import sys
print((sys.version))

if sys.version_info[0] < 3:
    print("This script requires Python version 3.x")
    sys.exit(1)


class Core():

    def __init__(self, ctrl):
        super(Core, self).__init__()
        self.ctrl = ctrl
        print("core")
