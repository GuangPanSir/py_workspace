import wx


class my_frame(wx.Frame):
    def __init__
    super().__init__(None, title='Hello', size=(300, 260))


app = wx.App()

frame = my_frame()

frame.Show()

app.MainLoop()
