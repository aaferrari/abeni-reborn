#!/usr/bin/env python
# -*- coding: ANSI_X3.4-1968 -*-
#
# generated by wxGlade HG on Sat May 24 09:11:12 2014
#

import wx

# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        
        # Menu Bar
        self.menubar = wx.MenuBar()
        global mnuNewID; mnuNewID = wx.NewId()
        global mnuLoadOverlayID; mnuLoadOverlayID = wx.NewId()
        global mnuLoadID; mnuLoadID = wx.NewId()
        global mnuSaveID; mnuSaveID = wx.NewId()
        global mnuDelID; mnuDelID = wx.NewId()
        global mnuExportID; mnuExportID = wx.NewId()
        global exitID; exitID = wx.NewId()
        global mnuFindID; mnuFindID = wx.NewId()
        global mnuFindAgainID; mnuFindAgainID = wx.NewId()
        global mnuAddFuncID; mnuAddFuncID = wx.NewId()
        global mnuLicenseID; mnuLicenseID = wx.NewId()
        global mnuCleanID; mnuCleanID = wx.NewId()
        global mnuDigestID; mnuDigestID = wx.NewId()
        global mnuUnpackID; mnuUnpackID = wx.NewId()
        global mnuCompileID; mnuCompileID = wx.NewId()
        global mnuInstallID; mnuInstallID = wx.NewId()
        global mnuQmergeID; mnuQmergeID = wx.NewId()
        global mnuEbuildID; mnuEbuildID = wx.NewId()
        global mnuEmergeID; mnuEmergeID = wx.NewId()
        global mnuRepoScanID; mnuRepoScanID = wx.NewId()
        global mnuPatchID; mnuPatchID = wx.NewId()
        global mnuImportID; mnuImportID = wx.NewId()
        global mnuDiffID; mnuDiffID = wx.NewId()
        global mnuRepoFullID; mnuRepoFullID = wx.NewId()
        global mnuFileCopyID; mnuFileCopyID = wx.NewId()
        global mnuXtermSID; mnuXtermSID = wx.NewId()
        global mnuXtermDID; mnuXtermDID = wx.NewId()
        global mnuXtermCVSID; mnuXtermCVSID = wx.NewId()
        self.mnuFullCommitID = wx.NewId()
        global mnuEditID; mnuEditID = wx.NewId()
        global mnuViewMetadataID; mnuViewMetadataID = wx.NewId()
        global mnuViewChangeLogID; mnuViewChangeLogID = wx.NewId()
        global mnuClearLogID; mnuClearLogID = wx.NewId()
        global mnuPrefID; mnuPrefID = wx.NewId()
        global mnuHelpID; mnuHelpID = wx.NewId()
        global mnuHelpRefID; mnuHelpRefID = wx.NewId()
        global mnuEclassID; mnuEclassID = wx.NewId()
        global mnuPrivID; mnuPrivID = wx.NewId()
        global mnuUseID; mnuUseID = wx.NewId()
        global mnulocalUseID; mnulocalUseID = wx.NewId()
        global mnuFKEYS_ID; mnuFKEYS_ID = wx.NewId()
        global mnuCVS_ID; mnuCVS_ID = wx.NewId()
        global mnuAboutID; mnuAboutID = wx.NewId()
        self.fileMenu = wx.Menu()
        self.fileMenu.Append(mnuNewID, _("&New ebuild\tCtrl-n"), "", wx.ITEM_NORMAL)
        self.fileMenu.Append(mnuLoadOverlayID, _("L&oad ebuild from PORTDIR_OVERLAY"), "", wx.ITEM_NORMAL)
        self.fileMenu.Append(mnuLoadID, _("&Load ebuild from PORTDIR"), "", wx.ITEM_NORMAL)
        self.fileMenu.Append(mnuSaveID, _("&Save ebuild\tCtrl-S"), "", wx.ITEM_NORMAL)
        self.fileMenu.Append(mnuDelID, _("&Delete this ebuild"), "", wx.ITEM_NORMAL)
        self.fileMenu.Append(mnuExportID, _("&Export ebuild and aux files to tar"), "", wx.ITEM_NORMAL)
        self.fileMenu.Append(exitID, _("E&xit\tAlt-X"), "", wx.ITEM_NORMAL)
        self.menubar.Append(self.fileMenu, _("&File"))
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(mnuFindID, _("&Find\tCtrl-F"), "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(mnuFindAgainID, _("Find a&gain\tCtrl-g"), "", wx.ITEM_NORMAL)
        self.menubar.Append(wxglade_tmp_menu, _("&Edit"))
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(mnuAddFuncID, _("&Function\tF6"), "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(mnuLicenseID, _("&License"), "", wx.ITEM_NORMAL)
        self.menubar.Append(wxglade_tmp_menu, _("&Insert"))
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(mnuCleanID, _("&Clean\tShift-F1"), "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(mnuDigestID, _("&Digest\tF1"), "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(mnuUnpackID, _("&Unpack\tF2"), "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(mnuCompileID, _("C&ompile\tF3"), "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(mnuInstallID, _("&Install\tF4"), "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(mnuQmergeID, _("&Qmerge\tF5"), "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(mnuEbuildID, _("&ebuild <this ebuild> command\tF9"), "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(mnuEmergeID, _("e&merge this ebuild\tF10"), "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(mnuRepoScanID, _("&Repoman scan"), "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(mnuPatchID, _("Create patch from source in ${S}"), "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(mnuImportID, _("&Import existing patch"), "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(mnuDiffID, _("diff of this ebuild against PORTDIR version"), "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(mnuRepoFullID, _("repoman full"), "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(mnuFileCopyID, _("${FILESDIR} copy/diff/edit/del\tF8"), "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(mnuXtermSID, _("xterm in ${S}\tF12"), "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(mnuXtermDID, _("xterm in ${D}"), "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(mnuXtermCVSID, _("xterm in CVS dir\tShift-F12"), "", wx.ITEM_NORMAL)
        self.menubar.Append(wxglade_tmp_menu, _("&Tools"))
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(self.mnuFullCommitID, _("repoman cvs commit"), "", wx.ITEM_NORMAL)
        self.menubar.Append(wxglade_tmp_menu, _("&CVS"))
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(mnuEditID, _("&ebuild in external editor\tF7"), "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(mnuViewMetadataID, _("metadata.&xml"), "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(mnuViewChangeLogID, _("Change&Log"), "", wx.ITEM_NORMAL)
        self.menubar.Append(wxglade_tmp_menu, _("&View"))
        self.menu_options = wx.Menu()
        self.menu_options.Append(mnuClearLogID, _("&Clear log window\tF11"), "", wx.ITEM_NORMAL)
        self.menubar.Append(self.menu_options, _("Lo&g"))
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(mnuPrefID, _("&Preferences"), "", wx.ITEM_NORMAL)
        self.menubar.Append(wxglade_tmp_menu, _("&Options"))
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(mnuHelpID, _("&Contents"), "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(mnuHelpRefID, _("Ebuild &Quick Reference"), "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(mnuEclassID, _("&eclasses"), "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(mnuPrivID, _("&Portage private functions"), "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(mnuUseID, _("USE variables"), "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(mnulocalUseID, _("&local USE variables"), "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(mnuFKEYS_ID, _("List &Fkeys"), "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(mnuCVS_ID, _("Gentoo repoman &CVS help"), "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(mnuAboutID, _("&About Abeni"), "", wx.ITEM_NORMAL)
        self.menubar.Append(wxglade_tmp_menu, _("&Help"))
        self.SetMenuBar(self.menubar)
        # Menu Bar end
        self.statusbar = self.CreateStatusBar(2, 0)
        
        # Tool Bar
        self.toolbar = wx.ToolBar(self, -1, style=wx.TB_HORIZONTAL | wx.TB_FLAT)
        self.SetToolBar(self.toolbar)
        global newID; newID = wx.NewId()
        global openID; openID = wx.NewId()
        global openOvlID; openOvlID = wx.NewId()
        global saveID; saveID = wx.NewId()
        global editID; editID = wx.NewId()
        global newFuncID; newFuncID = wx.NewId()
        global toolCleanID; toolCleanID = wx.NewId()
        global digestID; digestID = wx.NewId()
        global unpackID; unpackID = wx.NewId()
        global compileID; compileID = wx.NewId()
        global installID; installID = wx.NewId()
        global qmergeID; qmergeID = wx.NewId()
        global ebuildID; ebuildID = wx.NewId()
        global emergeID; emergeID = wx.NewId()
        global xtermID; xtermID = wx.NewId()
        self.StopID = wx.NewId()
        self.toolbar.AddLabelTool(newID, _("new"), wx.Bitmap("/usr/share/pixmaps/abeni/new.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, _("New ebuild"), "")
        self.toolbar.AddLabelTool(openID, _("open"), wx.Bitmap("/usr/share/pixmaps/abeni/open.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, _("Open ebuild in PORTDIR"), "")
        self.toolbar.AddLabelTool(openOvlID, _("openOvl"), wx.Bitmap("/usr/share/pixmaps/abeni/open_ovl.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, _("Open ebuild in PORTDIR_OVERLAY"), "")
        self.toolbar.AddLabelTool(saveID, _("save"), wx.Bitmap("/usr/share/pixmaps/abeni/save.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, _("Save ebuild Ctrl-S"), "")
        self.toolbar.AddLabelTool(editID, _("edit"), wx.Bitmap("/usr/share/pixmaps/abeni/edit.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, _("Edit ebuild in external editor F7"), "")
        self.toolbar.AddSeparator()
        self.toolbar.AddLabelTool(newFuncID, _("newFunc"), wx.Bitmap("/usr/share/pixmaps/abeni/fx.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, _("New Function F6"), "")
        self.toolbar.AddLabelTool(toolCleanID, _("clean"), wx.Bitmap("/usr/share/pixmaps/abeni/clean.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, _("Clean Shift-F1"), "")
        self.toolbar.AddLabelTool(digestID, _("digest"), wx.Bitmap("/usr/share/pixmaps/abeni/digest.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, _("Digest F1"), "")
        self.toolbar.AddLabelTool(unpackID, _("unpack"), wx.Bitmap("/usr/share/pixmaps/abeni/unpack.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, _("Unpack F2"), "")
        self.toolbar.AddLabelTool(compileID, _("compile"), wx.Bitmap("/usr/share/pixmaps/abeni/compile.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, _("Compile F3"), "")
        self.toolbar.AddLabelTool(installID, _("install"), wx.Bitmap("/usr/share/pixmaps/abeni/install.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, _("Install F4"), "")
        self.toolbar.AddLabelTool(qmergeID, _("qmerge"), wx.Bitmap("/usr/share/pixmaps/abeni/qmerge.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, _("Qmerge F5"), "")
        self.toolbar.AddLabelTool(ebuildID, _("ebuild"), wx.Bitmap("/usr/share/pixmaps/abeni/ebuild.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, _("ebuild <this ebuild> command F9"), "")
        self.toolbar.AddLabelTool(emergeID, _("emerge"), wx.Bitmap("/usr/share/pixmaps/abeni/emerge.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, _("emerge <options><this ebuild> F10"), "")
        self.toolbar.AddLabelTool(xtermID, _("xterm"), wx.Bitmap("/usr/share/pixmaps/abeni/xterm.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, _("Launch xterm in $S F12"), "")
        self.toolbar.AddSeparator()
        self.toolbar.AddLabelTool(self.StopID, _("stop"), wx.Bitmap("/usr/share/pixmaps/abeni/stop.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, _("Interrupt process running in log window"), "")
        # Tool Bar end
        self.static_line_2 = wx.StaticLine(self, wx.ID_ANY)
        self.panel_1 = wx.Panel(self, wx.ID_ANY)
        self.panel_cpvr = wx.Panel(self.panel_1, wx.ID_ANY)
        self.button_Category = wx.Button(self.panel_cpvr, wx.ID_ANY, _("Category"))
        self.text_ctrl_Category = wx.TextCtrl(self.panel_cpvr, wx.ID_ANY, "")
        self.label_PN = wx.StaticText(self.panel_cpvr, wx.ID_ANY, _("$PN"))
        self.text_ctrl_PN = wx.TextCtrl(self.panel_cpvr, wx.ID_ANY, "")
        self.label_PVR = wx.StaticText(self.panel_cpvr, wx.ID_ANY, _("$PVR"))
        self.text_ctrl_PVR = wx.TextCtrl(self.panel_cpvr, wx.ID_ANY, "")
        self.button_1 = wx.ToggleButton(self.panel_cpvr, wx.ID_ANY, _("noauto"))
        self.static_line_3 = wx.StaticLine(self.panel_1, wx.ID_ANY)
        self.splitter = wx.SplitterWindow(self.panel_1, wx.ID_ANY, style=wx.SP_3D | wx.SP_BORDER)
        self.STCeditor = GentooSTC(self.splitter, wx.ID_ANY)
        self.notebook_1 = wx.Notebook(self.splitter, wx.ID_ANY, style=wx.NB_BOTTOM)
        self.panel_log = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.text_ctrl_log = wx.TextCtrl(self.panel_log, wx.ID_ANY, "", style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.panel_explorer = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.window_1 = wx.SplitterWindow(self.panel_explorer, wx.ID_ANY, style=wx.SP_3DBORDER | wx.SP_BORDER)
        self.window_1_pane_1 = wx.Panel(self.window_1, wx.ID_ANY)
        global treeID; treeID = wx.NewId()
        self.tree_ctrl_1 = wx.TreeCtrl(self.window_1_pane_1, treeID, style=wx.SUNKEN_BORDER)
        self.window_1_pane_2 = wx.Panel(self.window_1, wx.ID_ANY)
        self.explorer = wx.GenericDirCtrl(self.window_1_pane_2, wx.ID_ANY, filter="All files|*")
        self.button_view = wx.Button(self.window_1_pane_2, wx.ID_ANY, _("View"))
        self.button_edit = wx.Button(self.window_1_pane_2, wx.ID_ANY, _("Edit"))
        self.button_patch = wx.Button(self.window_1_pane_2, wx.ID_ANY, _("Create patch"))
        self.button_delete = wx.Button(self.window_1_pane_2, wx.ID_ANY, _("Delete"))
        self.panel_environment = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.text_ctrl_environment = wx.TextCtrl(self.panel_environment, wx.ID_ANY, "", style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.button_env_refresh = wx.Button(self.panel_environment, wx.ID_ANY, _("Refresh"))
        self.radio_box_env = wx.RadioBox(self.panel_environment, wx.ID_ANY, _("View"), choices=[_("Brief"), _("Full")], majorDimension=1, style=wx.RA_SPECIFY_ROWS)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle(_("Abeni"))
        _icon = wx.EmptyIcon()
        _icon.CopyFromBitmap(wx.Bitmap("/usr/share/pixmaps/abeni/abeni_logo16.png", wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)
        self.SetSize((882, 696))
        self.statusbar.SetStatusWidths([-1, 400])
        # statusbar fields
        statusbar_fields = ["", ""]
        for i in range(len(statusbar_fields)):
            self.statusbar.SetStatusText(statusbar_fields[i], i)
        self.toolbar.Realize()
        self.button_Category.Enable(False)
        self.text_ctrl_Category.SetToolTip(wx.ToolTip(_("Select a category")))
        self.text_ctrl_Category.Enable(False)
        self.text_ctrl_PN.SetToolTip(wx.ToolTip(_("Enter the Package Name")))
        self.text_ctrl_PN.Enable(False)
        self.text_ctrl_PVR.SetToolTip(wx.ToolTip(_("Enter the Package Version")))
        self.text_ctrl_PVR.Enable(False)
        self.button_1.SetValue(1)
        self.radio_box_env.SetSelection(0)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_13 = wx.BoxSizer(wx.VERTICAL)
        sizer_14 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_9 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_11 = wx.BoxSizer(wx.VERTICAL)
        sizer_12 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_10 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4 = wx.BoxSizer(wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(self.static_line_2, 0, wx.EXPAND, 0)
        sizer_8.Add(self.button_Category, 0, wx.RIGHT, 10)
        sizer_8.Add(self.text_ctrl_Category, 1, wx.RIGHT | wx.EXPAND, 16)
        sizer_5.Add(sizer_8, 1, wx.EXPAND, 0)
        sizer_6.Add(self.label_PN, 0, wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, 10)
        sizer_6.Add(self.text_ctrl_PN, 1, wx.RIGHT | wx.EXPAND, 16)
        sizer_5.Add(sizer_6, 1, wx.EXPAND, 0)
        sizer_7.Add(self.label_PVR, 0, wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, 10)
        sizer_7.Add(self.text_ctrl_PVR, 0, 0, 0)
        sizer_5.Add(sizer_7, 1, wx.EXPAND, 0)
        sizer_5.Add(self.button_1, 0, wx.FIXED_MINSIZE, 0)
        sizer_3.Add(sizer_5, 1, wx.ALL, 6)
        self.panel_cpvr.SetSizer(sizer_3)
        sizer_2.Add(self.panel_cpvr, 0, wx.EXPAND, 0)
        sizer_2.Add(self.static_line_3, 0, wx.EXPAND, 0)
        sizer_4.Add(self.text_ctrl_log, 1, wx.EXPAND, 0)
        self.panel_log.SetSizer(sizer_4)
        sizer_10.Add(self.tree_ctrl_1, 1, wx.EXPAND, 0)
        self.window_1_pane_1.SetSizer(sizer_10)
        sizer_11.Add(self.explorer, 1, wx.EXPAND, 0)
        sizer_12.Add(self.button_view, 0, wx.LEFT, 8)
        sizer_12.Add(self.button_edit, 0, wx.LEFT, 8)
        sizer_12.Add(self.button_patch, 0, wx.LEFT, 8)
        sizer_12.Add(self.button_delete, 0, wx.LEFT, 8)
        sizer_11.Add(sizer_12, 0, wx.EXPAND, 0)
        self.window_1_pane_2.SetSizer(sizer_11)
        self.window_1.SplitVertically(self.window_1_pane_1, self.window_1_pane_2)
        sizer_9.Add(self.window_1, 1, wx.EXPAND, 0)
        self.panel_explorer.SetSizer(sizer_9)
        sizer_13.Add(self.text_ctrl_environment, 1, wx.EXPAND, 0)
        sizer_14.Add(self.button_env_refresh, 0, wx.ALL, 10)
        sizer_14.Add(self.radio_box_env, 0, wx.BOTTOM, 12)
        sizer_13.Add(sizer_14, 0, wx.EXPAND, 0)
        self.panel_environment.SetSizer(sizer_13)
        self.notebook_1.AddPage(self.panel_log, _("Output"))
        self.notebook_1.AddPage(self.panel_explorer, _("Files"))
        self.notebook_1.AddPage(self.panel_environment, _("Environment"))
        self.splitter.SplitHorizontally(self.STCeditor, self.notebook_1)
        sizer_2.Add(self.splitter, 1, wx.EXPAND, 0)
        self.panel_1.SetSizer(sizer_2)
        sizer_1.Add(self.panel_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        self.Centre()
        # end wxGlade

# end of class MyFrame
class MyApp(wx.App):
    def OnInit(self):
        wx.InitAllImageHandlers()
        frame_1 = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(frame_1)
        frame_1.Show()
        return 1

# end of class MyApp

if __name__ == "__main__":
    gettext.install("app") # replace with the appropriate catalog name

    app = MyApp(0)
    app.MainLoop()