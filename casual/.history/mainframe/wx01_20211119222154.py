import wx
"""
组件大概顺序：
    窗口
    面板
    文本等其他
"""


# 自定义窗口类
class my_frame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Hello", size=(400, 200), pos=(100, 200))
        panel = wx.Panel(parent=self)
        self.statictext = wx.StaticText(parent=panel,
                                        label='Hello World!',
                                        pos=(10, 10))
        b = wx.Button(parent=panel, label='OK', pos=(100, 50))
        self.Bind(wx.EVT_BUTTON, self.on_click, b)

        # 创建垂直方向的盒子布局管理器对象
        vbox = wx.BoxSizer(wx.VERTICAL)

        # 添加静态文本到vbox中
        vbox.Add(self.)


    def on_click(self, event):
        self.statictext.SetLabelText('你好，潘光健')


# 创建应用程序对象
app = wx.App()

# 创建窗口对象
frm = my_frame()

# 显示窗口
frm.Show()

# 进入主事件循环
app.MainLoop()
