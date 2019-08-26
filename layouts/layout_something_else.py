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
## Class SomethingElse
###########################################################################

class SomethingElse(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"Something Else  - Task Notifier", pos=wx.DefaultPosition,
                           size=wx.Size(478, 332), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        bSizer8 = wx.BoxSizer(wx.VERTICAL)

        bSizer8.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_staticText8 = wx.StaticText(self, wx.ID_ANY, u"Please enter your custom message", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText8.Wrap(-1)
        self.m_staticText8.SetFont(wx.Font(15, 70, 90, 92, False, wx.EmptyString))
        self.m_staticText8.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))

        bSizer8.Add(self.m_staticText8, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer9 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer9.Add((0, 0), 1, wx.EXPAND, 5)

        self.textCtrlMsg = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(350, 125), 0)
        self.textCtrlMsg.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        bSizer9.Add(self.textCtrlMsg, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer9.Add((0, 0), 1, wx.EXPAND, 5)

        bSizer8.Add(bSizer9, 1, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.buttonDoneItem = wx.Button(self, wx.ID_ANY, u"Done", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer8.Add(self.buttonDoneItem, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer8.Add((0, 0), 1, wx.EXPAND, 5)

        self.SetSizer(bSizer8)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.buttonDoneItem.Bind(wx.EVT_BUTTON, self.onFoodDoneClicked)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def onFoodDoneClicked(self, event):
        event.Skip()


