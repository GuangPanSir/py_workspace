import wx


class my_frame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Hello", size=(400, 200), pos=(100, 200))


app = wx.App()
