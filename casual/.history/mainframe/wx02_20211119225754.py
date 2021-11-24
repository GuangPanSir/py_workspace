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
        pwd = wx.StaticText(panel, label='密码')
        content = wx.StaticText(panel, label='多行文本')

        vbox = wx.BoxSizer(wx.VERTICAL)

        vbox.Add(userid, flag=wx.EXPAND | wx.LEFT, border=10)
        vbox.Add(tc1, flag=wx.EXPAND | wx.ALL, border=10)
        vbox.Add(pwd, flag=wx.EXPAND | wx.LEFT, border=10)
        vbox.Add(tc2, flag=wx.EXPAND | wx.ALL, border=10)
        vbox.Add(content, flag=wx.EXPAND | wx.LEFT, border=10)
        vbox.Add(tc3, flag=wx.EXPAND | wx.ALL, border=10)

        panel.SetSizer(vbox)

app = wx.App()

frame = my_frame()

frame.Show()

app.MainLoop()
