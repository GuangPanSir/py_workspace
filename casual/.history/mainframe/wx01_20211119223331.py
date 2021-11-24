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
        self.statictext = wx.StaticText(
            parent=panel,
            label='请单击按钮',
        )
        b1 = wx.Button(parent=panel, label='OK',)
        b1 = wx.Button(parent=panel, label='OK')
        self.Bind(wx.EVT_BUTTON, self.on_click, b)

        # 创建垂直方向的盒子布局管理器对象
        vbox = wx.BoxSizer(wx.VERTICAL)

        # 添加静态文本到vbox中
        vbox.Add(self.statictext,
                 proportion=1,
                 flag=wx.ALIGN_CENTER_HORIZONTAL | wx.FIXED_MINSIZE | wx.TOP,
                 border=30)
        # 添加按钮到vbox中
        vbox.Add(b, proportion=1, flag=wx.EXPAND | wx.BOTTOM, border=10)

        panel.SetSizer(vbox)

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
