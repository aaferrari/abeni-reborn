# generated by wxGlade HG on Sat May 24 09:38:14 2014
#
# To get wxPerl visit http://wxPerl.sourceforge.net/
#

use Wx 0.15 qw[:allclasses];
use strict;
# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade

package MyDialog;

use Wx qw[:everything];
use base qw(Wx::Dialog);
use strict;


sub new {
    my( $self, $parent, $id, $title, $pos, $size, $style, $name ) = @_;
    $parent = undef              unless defined $parent;
    $id     = -1                 unless defined $id;
    $title  = ""                 unless defined $title;
    $pos    = wxDefaultPosition  unless defined $pos;
    $size   = wxDefaultSize      unless defined $size;
    $name   = ""                 unless defined $name;

    # begin wxGlade: MyDialog::new
    $style = wxDEFAULT_DIALOG_STYLE 
        unless defined $style;

    $self = $self->SUPER::new( $parent, $id, $title, $pos, $size, $style, $name );
    $self->{label_1} = Wx::StaticText->new($self, wxID_ANY, _T("Enter name of herd:"), wxDefaultPosition, wxDefaultSize, );
    $self->{text_ctrl_herd} = Wx::TextCtrl->new($self, wxID_ANY, "", wxDefaultPosition, wxDefaultSize, wxTE_PROCESS_ENTER);
    $self->{button_herd} = Wx::Button->new($self, wxID_ANY, _T("Add"));
    $self->{list_box_herds} = Wx::ListBox->new($self, wxID_ANY, wxDefaultPosition, wxDefaultSize, [], );
    $self->{button_remove_herd} = Wx::Button->new($self, wxID_ANY, _T("Remove herd"));
    $self->{text_ctrl_long_desc} = Wx::TextCtrl->new($self, wxID_ANY, "", wxDefaultPosition, wxDefaultSize, wxTE_MULTILINE);
    $self->{sizer_11_staticbox} = Wx::StaticBox->new($self, wxID_ANY, _T("Long Description") );
    $self->{sizer_3_staticbox} = Wx::StaticBox->new($self, wxID_ANY, _T("Herds") );
    $self->{label_email} = Wx::StaticText->new($self, wxID_ANY, _T("Email address of maintainer"), wxDefaultPosition, wxDefaultSize, );
    $self->{text_ctrl_email} = Wx::TextCtrl->new($self, wxID_ANY, "", wxDefaultPosition, wxDefaultSize, );
    $self->{label_name} = Wx::StaticText->new($self, wxID_ANY, _T("Full name of maintainer (optional)"), wxDefaultPosition, wxDefaultSize, );
    $self->{text_ctrl_name} = Wx::TextCtrl->new($self, wxID_ANY, "", wxDefaultPosition, wxDefaultSize, );
    $self->{label_desc} = Wx::StaticText->new($self, wxID_ANY, _T("Description of maintainership"), wxDefaultPosition, wxDefaultSize, );
    $self->{text_ctrl_desc} = Wx::TextCtrl->new($self, wxID_ANY, "", wxDefaultPosition, wxDefaultSize, );
    $self->{button_remove_maintainer} = Wx::Button->new($self, wxID_ANY, _T("Clear All"));
    $self->{button_add_maintainer} = Wx::Button->new($self, wxID_ANY, _T("Add"));
    $self->{sizer_7_staticbox} = Wx::StaticBox->new($self, wxID_ANY, _T("Maintainer") );
    $self->{tree_ctrl_1} = Wx::TreeCtrl->new($self, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxTR_HAS_BUTTONS|wxTR_LINES_AT_ROOT|wxTR_DEFAULT_STYLE|wxSUNKEN_BORDER);
    $self->{stc} = GentooSTC->new($self, wxID_ANY);
    $self->{button_save} = Wx::Button->new($self, wxID_OK, _T("Save"));
    $self->{button_cancel} = Wx::Button->new($self, wxID_CANCEL, _T("Cancel"));
    $self->{button_preview} = Wx::Button->new($self, wxID_ANY, _T("Preview"));

    $self->__set_properties();
    $self->__do_layout();

    # end wxGlade
    return $self;

}


sub __set_properties {
    my $self = shift;
    # begin wxGlade: MyDialog::__set_properties
    $self->SetTitle(_T("metadata.xml"));
    $self->{list_box_herds}->SetSelection(0);
    # end wxGlade
}

sub __do_layout {
    my $self = shift;
    # begin wxGlade: MyDialog::__do_layout
    $self->{sizer_1} = Wx::BoxSizer->new(wxVERTICAL);
    $self->{sizer_9} = Wx::BoxSizer->new(wxHORIZONTAL);
    $self->{sizer_2} = Wx::BoxSizer->new(wxHORIZONTAL);
    $self->{sizer_6} = Wx::BoxSizer->new(wxVERTICAL);
    $self->{sizer_7_staticbox}->Lower();
    $self->{sizer_7} = Wx::StaticBoxSizer->new($self->{sizer_7_staticbox}, wxVERTICAL);
    $self->{sizer_8} = Wx::BoxSizer->new(wxHORIZONTAL);
    $self->{sizer_3_staticbox}->Lower();
    $self->{sizer_3} = Wx::StaticBoxSizer->new($self->{sizer_3_staticbox}, wxVERTICAL);
    $self->{sizer_10} = Wx::BoxSizer->new(wxHORIZONTAL);
    $self->{sizer_11_staticbox}->Lower();
    $self->{sizer_11} = Wx::StaticBoxSizer->new($self->{sizer_11_staticbox}, wxVERTICAL);
    $self->{sizer_4} = Wx::BoxSizer->new(wxVERTICAL);
    $self->{sizer_5} = Wx::BoxSizer->new(wxHORIZONTAL);
    $self->{sizer_4}->Add($self->{label_1}, 0, wxTOP, 12);
    $self->{sizer_5}->Add($self->{text_ctrl_herd}, 1, 0, 0);
    $self->{sizer_5}->Add($self->{button_herd}, 0, 0, 0);
    $self->{sizer_4}->Add($self->{sizer_5}, 0, wxALL|wxEXPAND, 6);
    $self->{sizer_3}->Add($self->{sizer_4}, 0, wxEXPAND, 0);
    $self->{sizer_3}->Add($self->{list_box_herds}, 1, wxALL|wxEXPAND, 6);
    $self->{sizer_3}->Add($self->{button_remove_herd}, 0, wxALL, 12);
    $self->{sizer_11}->Add($self->{text_ctrl_long_desc}, 1, wxALL|wxEXPAND, 6);
    $self->{sizer_10}->Add($self->{sizer_11}, 1, wxEXPAND, 0);
    $self->{sizer_3}->Add($self->{sizer_10}, 0, wxEXPAND, 0);
    $self->{sizer_2}->Add($self->{sizer_3}, 1, wxEXPAND, 0);
    $self->{sizer_7}->Add($self->{label_email}, 0, wxTOP, 12);
    $self->{sizer_7}->Add($self->{text_ctrl_email}, 0, wxALL|wxEXPAND, 4);
    $self->{sizer_7}->Add($self->{label_name}, 0, wxTOP, 4);
    $self->{sizer_7}->Add($self->{text_ctrl_name}, 0, wxALL|wxEXPAND, 6);
    $self->{sizer_7}->Add($self->{label_desc}, 0, wxTOP, 4);
    $self->{sizer_7}->Add($self->{text_ctrl_desc}, 0, wxALL|wxEXPAND, 6);
    $self->{sizer_8}->Add($self->{button_remove_maintainer}, 0, wxALL, 8);
    $self->{sizer_8}->Add($self->{button_add_maintainer}, 0, wxALL, 8);
    $self->{sizer_7}->Add($self->{sizer_8}, 0, wxEXPAND, 0);
    $self->{sizer_6}->Add($self->{sizer_7}, 1, wxEXPAND, 0);
    $self->{sizer_6}->Add($self->{tree_ctrl_1}, 1, wxEXPAND, 0);
    $self->{sizer_2}->Add($self->{sizer_6}, 1, wxEXPAND, 0);
    $self->{sizer_2}->Add($self->{stc}, 2, wxALL|wxEXPAND, 6);
    $self->{sizer_1}->Add($self->{sizer_2}, 0, wxEXPAND, 0);
    $self->{sizer_9}->Add($self->{button_save}, 0, wxALL, 20);
    $self->{sizer_9}->Add($self->{button_cancel}, 0, wxALL, 20);
    $self->{sizer_9}->Add($self->{button_preview}, 0, wxALL, 20);
    $self->{sizer_1}->Add($self->{sizer_9}, 0, wxEXPAND, 0);
    $self->SetSizer($self->{sizer_1});
    $self->{sizer_1}->Fit($self);
    $self->Layout();
    # end wxGlade
}

# end of class MyDialog

1;

