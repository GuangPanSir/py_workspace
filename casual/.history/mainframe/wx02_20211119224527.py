import wx


class my_frame(wx.Frame):
    super.__init__(None, title='Hello', size=(300, 260))

app = wx.App()

frame = 