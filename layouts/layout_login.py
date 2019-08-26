# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


###########################################################################
## Class LoginDialog
###########################################################################

class LoginDialog(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"Login - Task Notifier", pos=wx.DefaultPosition,
                           size=wx.Size(478, 332), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        bSizer8 = wx.BoxSizer(wx.VERTICAL)

        bSizer8.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_staticText8 = wx.StaticText(self, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText8.Wrap(-1)
        self.m_staticText8.SetFont(wx.Font(16, 70, 90, 92, False, wx.EmptyString))
        self.m_staticText8.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))

        bSizer8.Add(self.m_staticText8, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_staticText18 = wx.StaticText(self, wx.ID_ANY, u"Please Enter your Email & Password", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText18.Wrap(-1)
        self.m_staticText18.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_3DDKSHADOW))

        bSizer8.Add(self.m_staticText18, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer9 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer9.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_staticText3 = wx.StaticText(self, wx.ID_ANY, u"Email:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)
        self.m_staticText3.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))

        bSizer9.Add(self.m_staticText3, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.textCtrlEmail = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200, -1), 0)
        self.textCtrlEmail.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))

        bSizer9.Add(self.textCtrlEmail, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer9.Add((0, 0), 1, wx.EXPAND, 5)

        bSizer8.Add(bSizer9, 1, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer91 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer91.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_staticText31 = wx.StaticText(self, wx.ID_ANY, u"Password:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText31.Wrap(-1)
        self.m_staticText31.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))

        bSizer91.Add(self.m_staticText31, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.textCtrlPassword = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200, -1), 0)
        bSizer91.Add(self.textCtrlPassword, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer91.Add((0, 0), 1, wx.EXPAND, 5)

        bSizer8.Add(bSizer91, 1, wx.EXPAND, 5)

        self.buttonFoodDone = wx.Button(self, wx.ID_ANY, u"Enter", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer8.Add(self.buttonFoodDone, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer8.Add((0, 0), 1, wx.EXPAND, 5)

        self.SetSizer(bSizer8)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.buttonFoodDone.Bind(wx.EVT_BUTTON, self.onEnterClicked)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def onEnterClicked(self, event):
        event.Skip()


