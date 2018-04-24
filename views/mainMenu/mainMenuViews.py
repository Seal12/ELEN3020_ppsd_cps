import wx

from helpers import identityCodes


def create_menu_file():
    menu_file = wx.Menu()
    menu_file.Append(identityCodes.FILE_NEW_PROJECT, "New Project...")
    menu_file.Append(identityCodes.FILE_OPEN, "Open...")
    menu_file.Append(identityCodes.FILE_SAVE, "&Save")
    menu_file.Append(identityCodes.FILE_SAVE_AS, "&Save As...")
    menu_file.AppendSeparator()
    menu_file.Append(identityCodes.FILE_SETTINGS, "&Settings")
    menu_file.AppendSeparator()
    menu_file.Append(identityCodes.FILE_EXIT, "&Exit")

    return menu_file


def create_menu_edit():
    menu_edit = wx.Menu()
    menu_edit.Append(identityCodes.EDIT_UNDO, "&Undo...")
    menu_edit.Append(identityCodes.EDIT_REDO, "&Redo...")
    menu_edit.AppendSeparator()
    menu_edit.Append(identityCodes.EDIT_COPY, "&Copy")
    menu_edit.Append(identityCodes.EDIT_CUT, "&Cut")
    menu_edit.Append(identityCodes.EDIT_PASTE, "&Paste")
    menu_edit.AppendSeparator()
    menu_edit.Append(identityCodes.EDIT_FONT, "&Font...")
    
    return menu_edit


def create_menu_plot():
    menu_plot = wx.Menu()
    menu_plot.Append(identityCodes.PLOT_PCA, "&PCA")
    menu_plot.Append(identityCodes.PLOT_ADMIX, "&Structure/Admixture")

    return menu_plot


def create_menu_find():
    menu_find = wx.Menu()
    menu_find.Append(identityCodes.FIND_INDIVIDUAL, "&Individual")
    menu_find.Append(identityCodes.FIND_GROUP, "&Group")

    return menu_find


def create_menu_export():
    menu_export = wx.Menu()
    menu_export.Append(identityCodes.EXPORT_PDF, "&PDF")
    menu_export.Append(identityCodes.EXPORT_PNG, "&PNG")
    menu_export.Append(identityCodes.EXPORT_SVG, "&SVG")

    return menu_export


def create_menu_help():
    menu_help = wx.Menu()
    menu_help.Append(identityCodes.HELP_DOCUMENTATION, "&Documentation (link)")
    menu_help.Append(identityCodes.HELP_FAQ, "&FAQ (link)")
    menu_help.AppendSeparator()
    menu_help.Append(identityCodes.HELP_REPORT_ISSUE, "&Report Issue")
    menu_help.Append(identityCodes.HELP_FEEDBACK, "&Feedback")
    menu_help.AppendSeparator()
    menu_help.Append(identityCodes.HELP_CHECK_UPDATES, "&Check for Updates...")
    menu_help.Append(identityCodes.HELP_ABOUT, "&About")

    return menu_help
