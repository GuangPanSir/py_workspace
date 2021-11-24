import wx
from wx.core import BORDER
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
            label='你好，pan',
        )
        b1 = wx.Button(parent=panel, label='button1', id=10)
        b2 = wx.Button(parent=panel, label='button2', id=11)

        # 创建垂直方向的盒子布局管理器对象
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        hbox.Add(b1, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        hbox.Add(b2, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)

        vbox = wx.BoxSizer(wx.VERTICAL)

        # 添加静态文本到vbox中
        vbox.Add(self.statictext,
                 proportion=1,
                 flag=wx.ALIGN_CENTER_HORIZONTAL | wx.FIXED_MINSIZE | wx.TOP,
                 border=30)
        # 添加按钮到vbox中
        vbox.Add(hbox, proportion=1, flag=wx.CENTER)

        panel.SetSizer(vbox)

        self.Bind(wx.EVT_BUTTON, self.on_click, id=10, id2=20)

    def on_click(self, event):
        event_id = event.GetId()
        if event_id == 10:
            self.statictext.SetLabelText('你好明天')
        else:
            self.statictext.SetLabelText('你好生活')


# 创建应用程序对象
app = wx.App()

# 创建窗口对象
frm = my_frame()

# 显示窗口
frm.Show()

# 进入主事件循环
app.MainLoop()
