import wx


class my_frame(wx.Frame):
    def __init__(self):
        super().__init__(None, title='Hello', size=(300, 260), posi)


app = wx.App()

frame = my_frame()

frame.Show()

app.MainLoop()
