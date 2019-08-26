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
## Class HomeFrame
###########################################################################

class HomeFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Task Notifier", pos=wx.DefaultPosition,
                          size=wx.Size(635, 405), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        rowTitle = wx.BoxSizer(wx.HORIZONTAL)

        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, u"Task Notifier", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)
        self.m_staticText2.SetFont(wx.Font(25, 70, 90, 92, False, wx.EmptyString))
        self.m_staticText2.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))

        bSizer4.Add(self.m_staticText2, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        rowTitle.Add(bSizer4, 1, wx.EXPAND, 5)

        bSizer1.Add(rowTitle, 0, wx.EXPAND, 5)

        self.staticTextSendingAlert = wx.StaticText(self, wx.ID_ANY, u"Sending Noification. Please Wait...",
                                                    wx.DefaultPosition, wx.DefaultSize, 0)
        self.staticTextSendingAlert.Wrap(-1)
        self.staticTextSendingAlert.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))

        bSizer1.Add(self.staticTextSendingAlert, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer7 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer7.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_staticText21 = wx.StaticText(self, wx.ID_ANY, u"Recipient Email:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText21.Wrap(-1)
        bSizer7.Add(self.m_staticText21, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.textCtrlToEmail = wx.TextCtrl(self, wx.ID_ANY, u"virtualadamassistant@gmail.com", wx.DefaultPosition,
                                           wx.Size(250, -1), 0)
        bSizer7.Add(self.textCtrlToEmail, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer7.Add((0, 0), 1, wx.EXPAND, 5)

        bSizer1.Add(bSizer7, 1, wx.EXPAND, 5)

        rowOneOptions = wx.BoxSizer(wx.HORIZONTAL)

        rowOneOptions.Add((0, 0), 1, wx.EXPAND, 5)

        self.buttonMakeCoffee = wx.Button(self, wx.ID_ANY, u"Make Coffee", wx.DefaultPosition, wx.DefaultSize, 0)
        self.buttonMakeCoffee.SetFont(wx.Font(15, 70, 90, 90, False, wx.EmptyString))

        rowOneOptions.Add(self.buttonMakeCoffee, 0, wx.ALL, 5)

        self.buttonRefillBeverage = wx.Button(self, wx.ID_ANY, u"Refill Beverage", wx.DefaultPosition, wx.DefaultSize,
                                              0)
        self.buttonRefillBeverage.SetFont(wx.Font(15, 70, 90, 90, False, wx.EmptyString))

        rowOneOptions.Add(self.buttonRefillBeverage, 0, wx.ALL, 5)

        self.buttonMakeFood = wx.Button(self, wx.ID_ANY, u"Make Food", wx.DefaultPosition, wx.DefaultSize, 0)
        self.buttonMakeFood.SetFont(wx.Font(15, 70, 90, 90, False, wx.EmptyString))

        rowOneOptions.Add(self.buttonMakeFood, 0, wx.ALL, 5)

        self.buttonBringPills = wx.Button(self, wx.ID_ANY, u"Bring Pills", wx.DefaultPosition, wx.DefaultSize, 0)
        self.buttonBringPills.SetFont(wx.Font(15, 70, 90, 90, False, wx.EmptyString))

        rowOneOptions.Add(self.buttonBringPills, 0, wx.ALL, 5)

        rowOneOptions.Add((0, 0), 1, wx.EXPAND, 5)

        bSizer1.Add(rowOneOptions, 1, wx.EXPAND, 5)

        rowTwoOptions = wx.BoxSizer(wx.HORIZONTAL)

        rowTwoOptions.Add((0, 0), 1, wx.EXPAND, 5)

        self.buttonHelpGroceries = wx.Button(self, wx.ID_ANY, u"Help with Groceries", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.buttonHelpGroceries.SetFont(wx.Font(15, 70, 90, 90, False, wx.EmptyString))

        rowTwoOptions.Add(self.buttonHelpGroceries, 0, wx.ALL, 5)

        self.buttonBringSomething = wx.Button(self, wx.ID_ANY, u"Bring Something", wx.DefaultPosition, wx.DefaultSize,
                                              0)
        self.buttonBringSomething.SetFont(wx.Font(15, 70, 90, 90, False, wx.EmptyString))

        rowTwoOptions.Add(self.buttonBringSomething, 0, wx.ALL, 5)

        self.buttonHelpAmin = wx.Button(self, wx.ID_ANY, u"Help your Wife wth Amin", wx.DefaultPosition, wx.DefaultSize,
                                        0)
        self.buttonHelpAmin.SetFont(wx.Font(14, 70, 90, 90, False, wx.EmptyString))

        rowTwoOptions.Add(self.buttonHelpAmin, 0, wx.ALL, 5)

        rowTwoOptions.Add((0, 0), 1, wx.EXPAND, 5)

        bSizer1.Add(rowTwoOptions, 1, wx.EXPAND, 5)

        rowThreeOptions = wx.BoxSizer(wx.HORIZONTAL)

        rowThreeOptions.Add((0, 0), 1, wx.EXPAND, 5)

        rowThreeOptions.Add((0, 0), 1, wx.EXPAND, 5)

        self.buttonNeedTalk = wx.Button(self, wx.ID_ANY, u"Need to Talk", wx.DefaultPosition, wx.DefaultSize, 0)
        self.buttonNeedTalk.SetFont(wx.Font(15, 70, 90, 90, False, wx.EmptyString))

        rowThreeOptions.Add(self.buttonNeedTalk, 0, wx.ALL, 5)

        self.buttonPerformProfessional = wx.Button(self, wx.ID_ANY, u"Perform a Professional Massage",
                                                   wx.DefaultPosition, wx.DefaultSize, 0)
        self.buttonPerformProfessional.SetFont(wx.Font(14, 70, 90, 90, False, wx.EmptyString))

        rowThreeOptions.Add(self.buttonPerformProfessional, 0, wx.ALL, 5)

        self.buttonSomethingElse = wx.Button(self, wx.ID_ANY, u"Something Else", wx.DefaultPosition, wx.DefaultSize, 0)
        self.buttonSomethingElse.SetFont(wx.Font(15, 70, 90, 90, False, wx.EmptyString))

        rowThreeOptions.Add(self.buttonSomethingElse, 0, wx.ALL, 5)

        rowThreeOptions.Add((0, 0), 1, wx.EXPAND, 5)

        rowThreeOptions.Add((0, 0), 1, wx.EXPAND, 5)

        bSizer1.Add(rowThreeOptions, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.buttonMakeCoffee.Bind(wx.EVT_BUTTON, self.onClickMakeCoffee)
        self.buttonRefillBeverage.Bind(wx.EVT_BUTTON, self.onClickRefillBeverage)
        self.buttonMakeFood.Bind(wx.EVT_BUTTON, self.onClickMakeFood)
        self.buttonBringPills.Bind(wx.EVT_BUTTON, self.onClickBringPills)
        self.buttonHelpGroceries.Bind(wx.EVT_BUTTON, self.onClickHelpGroceries)
        self.buttonBringSomething.Bind(wx.EVT_BUTTON, self.onClickBringSomething)
        self.buttonHelpAmin.Bind(wx.EVT_BUTTON, self.onClickHelpAmin)
        self.buttonNeedTalk.Bind(wx.EVT_BUTTON, self.onClickNeedTalk)
        self.buttonPerformProfessional.Bind(wx.EVT_BUTTON, self.onClickProfMassage)
        self.buttonSomethingElse.Bind(wx.EVT_BUTTON, self.onClickSomethingElse)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def onClickMakeCoffee(self, event):
        event.Skip()

    def onClickRefillBeverage(self, event):
        event.Skip()

    def onClickMakeFood(self, event):
        event.Skip()

    def onClickBringPills(self, event):
        event.Skip()

    def onClickHelpGroceries(self, event):
        event.Skip()

    def onClickBringSomething(self, event):
        event.Skip()

    def onClickHelpAmin(self, event):
        event.Skip()

    def onClickNeedTalk(self, event):
        event.Skip()

    def onClickProfMassage(self, event):
        event.Skip()

    def onClickSomethingElse(self, event):
        event.Skip()


