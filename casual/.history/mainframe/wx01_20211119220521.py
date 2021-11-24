import wx


# 自定义窗口类
class my_frame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Hello", size=(400, 200), pos=(100, 200))
        panel = wx.panel(parent=self)
        statictext = wx.StaticText(parent=)


# 创建应用程序对象
app = wx.App()

# 创建窗口对象
frm = my_frame()

# 显示窗口
frm.Show()

# 进入主事件循环
app.MainLoop()
