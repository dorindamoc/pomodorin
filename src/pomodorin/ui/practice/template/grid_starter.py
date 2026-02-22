import wx


class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="GridSizer Example", size=wx.Size(400, 300))

        panel = wx.Panel(self)

        grid = wx.GridSizer(rows=2, cols=2, hgap=5, vgap=5)

        grid.Add(wx.Button(panel, label="A"), 0, wx.EXPAND)
        grid.Add(wx.Button(panel, label="B"), 0, wx.EXPAND)
        grid.Add(wx.Button(panel, label="C"), 0, wx.EXPAND)
        grid.Add(wx.Button(panel, label="D"), 0, wx.EXPAND)

        panel.SetSizer(grid)

        self.Centre()
        self.Show()


class MyApp(wx.App):
    def OnInit(self):
        self.frame = MainFrame()
        return True


if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()
