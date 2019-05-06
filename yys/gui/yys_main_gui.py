# coding:utf-8
from tkinter import *

__all__ = ['YYSMainGUI']

class YYSMainGUI(object):

    def __init__(self, device_config):
        self.config = device_config
        self.device_id = device_config.get('device_id')
        self.device_size = device_config.get('device_size')

    def showWindow(self):
        window = Tk()
        window.title("阴阳师辅助")
        window.geometry('600x350')
        lbl = Label(window, text="请输入截图后的图片名：")
        lbl.grid(column=0, row=0)
        txt = Entry(window, width=10)
        txt.grid(column=1, row=0)

        lbl_guidance = Label(window, text="请先输入需要截图的图片名称，坐标和截图会自动保存")
        lbl_guidance.grid(row=1)

        def clicked():
            if txt.get() == '':
                lbl.configure(text="请输入图片名称：")
                return
            lbl.configure(text="截图成功，图片名为：" + txt.get())
            self._save_image_show_crop(txt.get())

        btn = Button(window, text="截图", command=clicked)
        btn.grid(column=2, row=0)
        window.mainloop()
