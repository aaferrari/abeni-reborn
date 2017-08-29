# -*- coding: ANSI_X3.4-1968 -*-
#
# generated by wxGlade HG on Sat May 24 09:37:51 2014
#

from wxPython.wx import *
# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MyDialog(wxDialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyDialog.__init__
        kwds["style"] = wxDEFAULT_DIALOG_STYLE
        wxDialog.__init__(self, *args, **kwds)
        self.label_1 = wxStaticText(self, wxID_ANY, _("Enter name of herd:"))
        self.text_ctrl_herd = wxTextCtrl(self, wxID_ANY, "", style=wxTE_PROCESS_ENTER)
        self.button_herd = wxButton(self, wxID_ANY, _("Add"))
        self.list_box_herds = wxListBox(self, wxID_ANY, choices=[])
        self.button_remove_herd = wxButton(self, wxID_ANY, _("Remove herd"))
        self.text_ctrl_long_desc = wxTextCtrl(self, wxID_ANY, "", style=wxTE_MULTILINE)
        self.sizer_11_staticbox = wxStaticBox(self, wxID_ANY, _("Long Description"))
        self.sizer_3_staticbox = wxStaticBox(self, wxID_ANY, _("Herds"))
        self.label_email = wxStaticText(self, wxID_ANY, _("Email address of maintainer"))
        self.text_ctrl_email = wxTextCtrl(self, wxID_ANY, "")
        self.label_name = wxStaticText(self, wxID_ANY, _("Full name of maintainer (optional)"))
        self.text_ctrl_name = wxTextCtrl(self, wxID_ANY, "")
        self.label_desc = wxStaticText(self, wxID_ANY, _("Description of maintainership"))
        self.text_ctrl_desc = wxTextCtrl(self, wxID_ANY, "")
        self.button_remove_maintainer = wxButton(self, wxID_ANY, _("Clear All"))
        self.button_add_maintainer = wxButton(self, wxID_ANY, _("Add"))
        self.sizer_7_staticbox = wxStaticBox(self, wxID_ANY, _("Maintainer"))
        self.tree_ctrl_1 = wxTreeCtrl(self, wxID_ANY, style=wxTR_HAS_BUTTONS | wxTR_LINES_AT_ROOT | wxTR_DEFAULT_STYLE | wxSUNKEN_BORDER)
        self.stc = GentooSTC(self, wxID_ANY)
        self.button_save = wxButton(self, wxID_OK, _("Save"))
        self.button_cancel = wxButton(self, wxID_CANCEL, _("Cancel"))
        self.button_preview = wxButton(self, wxID_ANY, _("Preview"))

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyDialog.__set_properties
        self.SetTitle(_("metadata.xml"))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyDialog.__do_layout
        sizer_1 = wxBoxSizer(wxVERTICAL)
        sizer_9 = wxBoxSizer(wxHORIZONTAL)
        sizer_2 = wxBoxSizer(wxHORIZONTAL)
        sizer_6 = wxBoxSizer(wxVERTICAL)
        self.sizer_7_staticbox.Lower()
        sizer_7 = wxStaticBoxSizer(self.sizer_7_staticbox, wxVERTICAL)
        sizer_8 = wxBoxSizer(wxHORIZONTAL)
        self.sizer_3_staticbox.Lower()
        sizer_3 = wxStaticBoxSizer(self.sizer_3_staticbox, wxVERTICAL)
        sizer_10 = wxBoxSizer(wxHORIZONTAL)
        self.sizer_11_staticbox.Lower()
        sizer_11 = wxStaticBoxSizer(self.sizer_11_staticbox, wxVERTICAL)
        sizer_4 = wxBoxSizer(wxVERTICAL)
        sizer_5 = wxBoxSizer(wxHORIZONTAL)
        sizer_4.Add(self.label_1, 0, wxTOP, 12)
        sizer_5.Add(self.text_ctrl_herd, 1, 0, 0)
        sizer_5.Add(self.button_herd, 0, 0, 0)
        sizer_4.Add(sizer_5, 0, wxALL | wxEXPAND, 6)
        sizer_3.Add(sizer_4, 0, wxEXPAND, 0)
        sizer_3.Add(self.list_box_herds, 1, wxALL | wxEXPAND, 6)
        sizer_3.Add(self.button_remove_herd, 0, wxALL, 12)
        sizer_11.Add(self.text_ctrl_long_desc, 1, wxALL | wxEXPAND, 6)
        sizer_10.Add(sizer_11, 1, wxEXPAND, 0)
        sizer_3.Add(sizer_10, 0, wxEXPAND, 0)
        sizer_2.Add(sizer_3, 1, wxEXPAND, 0)
        sizer_7.Add(self.label_email, 0, wxTOP, 12)
        sizer_7.Add(self.text_ctrl_email, 0, wxALL | wxEXPAND, 4)
        sizer_7.Add(self.label_name, 0, wxTOP, 4)
        sizer_7.Add(self.text_ctrl_name, 0, wxALL | wxEXPAND, 6)
        sizer_7.Add(self.label_desc, 0, wxTOP, 4)
        sizer_7.Add(self.text_ctrl_desc, 0, wxALL | wxEXPAND, 6)
        sizer_8.Add(self.button_remove_maintainer, 0, wxALL, 8)
        sizer_8.Add(self.button_add_maintainer, 0, wxALL, 8)
        sizer_7.Add(sizer_8, 0, wxEXPAND, 0)
        sizer_6.Add(sizer_7, 1, wxEXPAND, 0)
        sizer_6.Add(self.tree_ctrl_1, 1, wxEXPAND, 0)
        sizer_2.Add(sizer_6, 1, wxEXPAND, 0)
        sizer_2.Add(self.stc, 2, wxALL | wxEXPAND, 6)
        sizer_1.Add(sizer_2, 0, wxEXPAND, 0)
        sizer_9.Add(self.button_save, 0, wxALL, 20)
        sizer_9.Add(self.button_cancel, 0, wxALL, 20)
        sizer_9.Add(self.button_preview, 0, wxALL, 20)
        sizer_1.Add(sizer_9, 0, wxEXPAND, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade

# end of class MyDialog