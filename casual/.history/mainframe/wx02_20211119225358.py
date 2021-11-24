import wx
from wx.core import Panel, Position


class my_frame(wx.Frame):
    def __init__(self):
        super().__init__(None, title='Hello', size=(300, 260), pos=(600, 300))
        panel = wx.Panel(parent=self)
        tc1 = wx.TextCtrl(panel)
        tc2 = wx.TextCtrl(panel, style=wx.TE_PASSWORD)
        tc3 = wx.TextCtrl(panel, style=wx.TE_MULTILINE)

        userid = wx.StaticText(panel, label='用户id')
        pwd = wx.StaticText(panel, labbel)


app = wx.App()

frame = my_frame()

frame.Show()

app.MainLoop()
