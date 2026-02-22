import wx


class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Note App", size=wx.Size(400, 300))

        panel = wx.Panel(self)

        # --- Sizer setup ---
        sizer = wx.BoxSizer(wx.VERTICAL)

        # Example widget
        label = wx.StaticText(panel, label="This is a note-taking app.")
        sizer.Add(label, 0, wx.ALL, 10)

        # Text control for note input
        self.text_ctrl = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
        sizer.Add(self.text_ctrl, 1, wx.EXPAND | wx.ALL, 10)
        
        buttons = Buttons(panel, self.text_ctrl)
        sizer.Add(buttons, 0, wx.ALL | wx.CENTER, 10)

        panel.SetSizer(sizer)

        self.Centre()
        self.Show()


class Buttons(wx.Panel):
    def __init__(self, parent, text_ctrl: wx.TextCtrl):
        super().__init__(parent)
        self.text_ctrl = text_ctrl

        sizer = wx.BoxSizer(wx.HORIZONTAL)

        save_button = wx.Button(self, label="Save Note")
        save_button.Bind(wx.EVT_BUTTON, self.on_save)
        sizer.Add(save_button, 0, wx.ALL | wx.CENTER, 10)

        load_button = wx.Button(self, label="Load Note")
        load_button.Bind(wx.EVT_BUTTON, self.on_load)
        sizer.Add(load_button, 0, wx.ALL | wx.CENTER, 10)

        self.SetSizer(sizer)

    def on_save(self, event):
        note_content  = self.text_ctrl.GetValue()
        with open("note.txt", "w") as file:
            file.write(note_content)
        wx.MessageBox("Note saved!", "Info", wx.OK | wx.ICON_INFORMATION)    

    def on_load(self, event):
        try:
            with open("note.txt", "r") as file:
                note_content = file.read()
                self.text_ctrl.SetValue(note_content)
            wx.MessageBox("Note loaded!", "Info", wx.OK | wx.ICON_INFORMATION)
        except FileNotFoundError:
            wx.MessageBox("No saved note found.", "Error", wx.OK | wx.ICON_ERROR)


class NoteApp(wx.App):
    def OnInit(self):
        self.frame = MainFrame()
        return True

if __name__ == "__main__":
    app = NoteApp()
    app.MainLoop()