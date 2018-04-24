import os
import wx


def get_file_dir(parent, file_type, extension):
    wildcard = "%s (*%s)|*%s" % (file_type, extension, extension)
    dialog = wx.FileDialog(parent, "Choose file...", wildcard=wildcard, style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

    if dialog.ShowModal() == wx.ID_CANCEL:
        return

    path = dialog.GetPath()

    if os.path.exists():
        return path
    else:
        return  # show some error messaage
