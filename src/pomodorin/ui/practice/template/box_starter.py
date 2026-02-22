import wx


class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="My wxPython App", size=wx.Size(400, 300))

        panel = wx.Panel(self)

        # --- Sizer setup ---
        sizer = wx.BoxSizer(wx.VERTICAL)

        # Example widget
        label = wx.StaticText(panel, label="Hello, wxPython!")
        sizer.Add(label, 0, wx.ALL, 10)

        panel.SetSizer(sizer)

        self.Centre()
        self.Show()


class MyApp(wx.App):
    def OnInit(self):
        self.frame = MainFrame()
        return True


if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()
