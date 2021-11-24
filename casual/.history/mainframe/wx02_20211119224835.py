import wx
from wx.core import Position


class my_frame(wx.Frame):
    def __init__(self):
        super().__init__(None, title='Hello', size=(300, 260), pos=(400, 200))


app = wx.App()

frame = my_frame()

frame.Show()

app.MainLoop()
