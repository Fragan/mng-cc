#!/usr/bin/python3

import sys
print((sys.version))

if sys.version_info[0] < 3:
    print("This script requires Python version 3.x")
    sys.exit(1)

import tkinter as MTk


# Tk inheritance
class Ui(MTk.Tk):

    def __init__(self, ctrl):
        print("ui")

        MTk.Tk.__init__(self, None)
        self.ctrl = ctrl
        self.initialize()

    def initialize(self):
        self.wm_title("MiniGal Nano Content Comment")
        self.grid()

        ########
        self.path_lbl = MTk.Label(self, text="Gallery\'s path:", anchor="w", fg="black")
        self.path_lbl.grid(column=0, row=0, columnspan=2, padx=4, sticky='EW')

        self.path_txt = MTk.StringVar()
        self.path_txt_line = MTk.Entry(self, textvariable=self.path_txt, width=90)
        self.path_txt_line.grid(column=0, row=1, sticky='EW')

        self.browse_btn = MTk.Button(self, text="Browse", command=self.ctrl.p2c_browse)
        self.browse_btn.grid(column=1, row=1, sticky='EW')

        ########
        self.gtitle_lbl = MTk.Label(self, text="Gallery\'s title:", anchor="w", fg="black")
        self.gtitle_lbl.grid(column=0, row=2, columnspan=2, padx=4, pady=6, sticky='EW')

        self.gtitle_txt = MTk.StringVar()
        self.gtitle_line = MTk.Entry(self, textvariable=self.gtitle_txt, width=90)
        self.gtitle_line.grid(column=0, row=3, sticky='EW')

        ########
        self.content_lbl = MTk.Label(self, text="Gallery\'s content:", anchor="w", fg="black")
        self.content_lbl.grid(column=0, row=4, columnspan=2, padx=4, pady=6, sticky='EW')

        self.content_panel = MTk.Frame(self)
        self.content_panel.grid(column=0, row=5, sticky='EW')

        self.content_scrollbar = MTk.Scrollbar(self.content_panel)
        self.content_scrollbar.pack(side=MTk.RIGHT, fill=MTk.Y)

        self.content_line = MTk.Text(self.content_panel, height=3, width=100, borderwidth=3, relief="sunken",
            yscrollcommand=self.content_scrollbar.set)
        self.content_line.pack(side=MTk.LEFT, fill=MTk.BOTH)

        self.content_scrollbar.config(command=self.content_line.yview)

        ########
        self.comment_lbl = MTk.Label(self, text="Image comment:", anchor="w", fg="black")
        self.comment_lbl.grid(column=0, row=6, columnspan=2, padx=4, pady=6, sticky='EW')

        self.comment_panel = MTk.Frame(self)
        self.comment_panel.grid(column=0, row=7, sticky='EW')

        self.comment_scrollbar = MTk.Scrollbar(self.comment_panel)
        self.comment_scrollbar.pack(side=MTk.RIGHT, fill=MTk.Y)

        self.comment_line = MTk.Text(self.comment_panel, height=3, width=100, borderwidth=3, relief="sunken",
            yscrollcommand=self.comment_scrollbar.set)
        self.comment_line.pack(side=MTk.LEFT, fill=MTk.BOTH)

        self.comment_scrollbar.config(command=self.content_line.yview)

        ########
        self.image_lbl = MTk.Label(self, width=100, height=60, bg="black", padx=4, pady=4)
        self.image_lbl.grid(column=0, row=8, sticky='EW')

        self.img_btn_panel = MTk.Frame(self)
        self.img_btn_panel.grid(column=1, row=8, sticky='NW')

        self.nxt_img_btn = MTk.Button(self.img_btn_panel, text="Next", command=self.ctrl.p2c_next)
        self.nxt_img_btn.pack(anchor="n")

        self.nxt_img_btn = MTk.Button(self.img_btn_panel, text="Previous", command=self.ctrl.p2c_previous)
        self.nxt_img_btn.pack(anchor="s")

        ########
        self.grid_columnconfigure(0, weight=1)
        self.update()
        # Freez dynamic window size
        self.geometry(self.geometry())

        # show view
        self.mainloop()
        self.destroy()

    def dispay_picture(self, img_path):
        img = MTk.PhotoImage(file=img_path)
        self.image_lbl.configure(image=img)

    def setPath(self, path):
        self.path_txt.insert(0, "")
        self.path_txt.insert(0, path)