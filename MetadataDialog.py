#!/usr/bin/env python
# generated by wxGlade 0.3.3 on Wed Jul 21 22:39:01 2004

import os

from wxPython.wx import *
from wxPython.stc import *

class MetadataDialog(wxDialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MetadataDialog.__init__
        kwds["style"] = wxDEFAULT_DIALOG_STYLE
        wxDialog.__init__(self, *args, **kwds)
        self.notebook_1 = wxNotebook(self, -1, style=0)
        self.notebook_1_pane_2 = wxPanel(self.notebook_1, -1)
        self.notebook_1_pane_1 = wxPanel(self.notebook_1, -1)
        self.metadata_out = wxStyledTextCtrl(self.notebook_1_pane_1, -1)
        self.sample = wxStyledTextCtrl(self.notebook_1_pane_2, -1)
        self.button_save = wxButton(self, wxID_OK, "Save")
        self.button_cancel = wxButton(self, wxID_CANCEL, "Cancel")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MetadataDialog.__set_properties
        self.SetTitle("metadata.xml")
        self.SetSize((400, 300))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MetadataDialog.__do_layout
        sizer_1 = wxBoxSizer(wxVERTICAL)
        sizer_2 = wxBoxSizer(wxHORIZONTAL)
        sizer_3 = wxBoxSizer(wxHORIZONTAL)
        sizer_4 = wxBoxSizer(wxHORIZONTAL)
        sizer_4.Add(self.metadata_out, 1, wxEXPAND, 0)
        self.notebook_1_pane_1.SetAutoLayout(1)
        self.notebook_1_pane_1.SetSizer(sizer_4)
        sizer_4.Fit(self.notebook_1_pane_1)
        sizer_4.SetSizeHints(self.notebook_1_pane_1)
        sizer_3.Add(self.sample, 1, wxEXPAND, 0)
        self.notebook_1_pane_2.SetAutoLayout(1)
        self.notebook_1_pane_2.SetSizer(sizer_3)
        sizer_3.Fit(self.notebook_1_pane_2)
        sizer_3.SetSizeHints(self.notebook_1_pane_2)
        self.notebook_1.AddPage(self.notebook_1_pane_1, "metadata.xml")
        self.notebook_1.AddPage(self.notebook_1_pane_2, "sample")
        sizer_1.Add(wxNotebookSizer(self.notebook_1), 1, wxALL|wxEXPAND, 8)
        sizer_2.Add(self.button_save, 0, wxLEFT, 80)
        sizer_2.Add(self.button_cancel, 0, wxLEFT, 60)
        sizer_1.Add(sizer_2, 0, wxALL|wxEXPAND, 8)
        self.SetAutoLayout(1)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

        #TODO: color/lex doesn't work
        skel = open("/usr/portage/skel.metadata.xml").read()
        self.metadata_out.EmptyUndoBuffer()
        self.metadata_out.SetMarginType(1, wxSTC_MARGIN_NUMBER)
        self.metadata_out.SetMarginWidth(1, 25)
        self.metadata_out.SetLexer(wxSTC_LEX_XML)
        self.sample.SetMarginType(1, wxSTC_MARGIN_NUMBER)
        self.sample.SetMarginWidth(1, 25)
        self.sample.SetLexer(wxSTC_LEX_XML)
        self.sample.SetText(skel)
        self.sample.SetReadOnly(1)
# end of class MetadataDialog

