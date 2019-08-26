import wx
from layouts import layout_home, layout_food_dialog, layout_bring_something_dialog, layout_something_else, \
    layout_login
from controllers.MailController import MailController
import datetime


class AppFrame(layout_home.HomeFrame):

    def __init__(self, parent):
        layout_home.HomeFrame.__init__(self, parent)
        self.from_email = ""
        self.from_pass = ""
        self.staticTextSendingAlert.Show(False)
        while len(self.from_email) < 1 or len(self.from_pass) < 1:
            login_dialog = LoginDialogUI(None)
            login_dialog.ShowModal()

            self.from_email = login_dialog.result[0]
            self.from_pass = login_dialog.result[1]

        if datetime.date.today().day == 17 and datetime.date.today().month == 6:
            msg_txt = "Happy Birthday!!! \n\nFrom Your Loving Son. - Adam"
            MailController().send_mail(msg_txt, self.from_email, self.from_pass, self.from_email)

        self.msg_ending = '''\n
With Love,
Your Father!
'''

    def send_notification(self, msg_txt, from_email, from_pass, to_email):
        self.staticTextSendingAlert.Show(True)
        self.Update()
        MailController().send_mail(msg_txt, from_email, from_pass, to_email)
        self.staticTextSendingAlert.Show(False)
        self.Update()

    def onClickMakeCoffee(self, event):
        msg_txt = "Hey! Can you please make a coffee for me?"
        msg_txt = msg_txt + self.msg_ending
        self.send_notification(msg_txt, self.from_email, self.from_pass, self.textCtrlToEmail.GetValue())

    def onClickRefillBeverage(self, event):
        msg_txt = "Hey! Can you please refill the beverage?"
        msg_txt = msg_txt + self.msg_ending
        self.send_notification(msg_txt, self.from_email, self.from_pass, self.textCtrlToEmail.GetValue())

    def onClickMakeFood(self, event):

        food_dialog = FoodDialogUI(None)
        food_dialog.ShowModal()

        if food_dialog.result[0] is not None and food_dialog.result[1] is not None and food_dialog.result[2] is not None:
            msg_txt = "Hey! I wanna have some food. " + \
                      "\nFood: " + food_dialog.result[0] + \
                      "\nSauce: " + food_dialog.result[1] + \
                      "\nMicro Wave Time: " + food_dialog.result[2]
            msg_txt = msg_txt + self.msg_ending

            self.send_notification(msg_txt, self.from_email, self.from_pass, self.textCtrlToEmail.GetValue())

    def onClickBringPills(self, event):
        msg_txt = "Hey! I need my pills. Can you please bring them over?"
        msg_txt = msg_txt + self.msg_ending
        self.send_notification(msg_txt, self.from_email, self.from_pass, self.textCtrlToEmail.GetValue())

    def onClickHelpGroceries(self, event):
        msg_txt = "Hey! Can you please help me out with groceries?"
        msg_txt = msg_txt + self.msg_ending
        self.send_notification(msg_txt, self.from_email, self.from_pass, self.textCtrlToEmail.GetValue())

    def onClickBringSomething(self, event):
        # item_name = input("Please Enter item name you want him to bring: ")
        # msg_txt = "Hey! Can you please bring " + item_name + " for me?"

        item_dialog = BringSomethingDialogUI(None)
        item_dialog.ShowModal()

        if item_dialog.result[0] is not None:
            msg_txt = "Hey! Can you please bring " + item_dialog.result[0] + " for me?"
            msg_txt = msg_txt + self.msg_ending
            self.send_notification(msg_txt, self.from_email, self.from_pass, self.textCtrlToEmail.GetValue())

    def onClickHelpAmin(self, event):
        msg_txt = "Hey! Can you please help your wife with Amin today?"
        msg_txt = msg_txt + self.msg_ending
        self.send_notification(msg_txt, self.from_email, self.from_pass, self.textCtrlToEmail.GetValue())

    def onClickNeedTalk(self, event):
        msg_txt = "Hey! Can you please come? I need to talk to you."
        msg_txt = msg_txt + self.msg_ending
        self.send_notification(msg_txt, self.from_email, self.from_pass, self.textCtrlToEmail.GetValue())

    def onClickProfMassage(self, event):
        msg_txt = "Hey! Can you please perform a professional massage? I'd really love to have one."
        msg_txt = msg_txt + self.msg_ending
        self.send_notification(msg_txt, self.from_email, self.from_pass, self.textCtrlToEmail.GetValue())

    def onClickSomethingElse(self, event):
        item_dialog = SomethingElseDialogUI(None)
        item_dialog.ShowModal()

        if item_dialog.result[0] is not None:
            msg_txt = item_dialog.result[0] + self.msg_ending
            self.send_notification(msg_txt, self.from_email, self.from_pass, self.textCtrlToEmail.GetValue())


class FoodDialogUI(layout_food_dialog.FoodDialog):
    def __init__(self, parent):
        layout_food_dialog.FoodDialog.__init__(self, parent)
        self.result = [None, None, None]

    def onFoodDoneClicked(self, event):
        self.result = [self.textCtrlFoodName.GetValue(), self.textCtrlSauceName.GetValue(), self.textCtrlMicroTime.GetValue()]
        self.Destroy()


class BringSomethingDialogUI(layout_bring_something_dialog.BringSomethingDialog):
    def __init__(self, parent):
        layout_bring_something_dialog.BringSomethingDialog.__init__(self, parent)
        self.result = [None]

    def onFoodDoneClicked(self, event):
        self.result = [self.textCtrlItemName.GetValue()]
        self.Destroy()


class SomethingElseDialogUI(layout_something_else.SomethingElse):
    def __init__(self, parent):
        layout_something_else.SomethingElse.__init__(self, parent)
        self.result = [None]

    def onFoodDoneClicked(self, event):
        self.result = [self.textCtrlMsg.GetValue()]
        self.Destroy()


class LoginDialogUI(layout_login.LoginDialog):
    def __init__(self, parent):
        layout_login.LoginDialog.__init__(self, parent)
        self.result = ["", ""]

    def onEnterClicked(self, event):
        self.result = [self.textCtrlEmail.GetValue(), self.textCtrlPassword.GetValue()]
        self.Destroy()


app = wx.App(False)
frame = AppFrame(None)
frame.Show(True)
app.MainLoop()
