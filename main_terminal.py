from controllers.MailController import MailController

menu_text = ''' *** Task Notifier ***

1. Make Coffee
2. Refill Beverage
3. Make Food
4. Bring Pills
5. Help With Groceries
6. Bring Something
7. Help Your Wife with Amin
8. Perform a Profesional Massage
9. Need to talk
10. Something else
11. Exit
'''

print("Welcome " + "Aladdin" + "!\n")

from_email = 
from_pass = input("Enter your password: ")
to_email = input("Enter recipients email: ")

msg_txt = ""
msg_ending = '''\n
With Love,
Your Father!
'''

while True:
    choice = int(input(menu_text))
    if choice is 1:
        msg_txt = "Hey! Can you please make a coffee for me?"
    elif choice is 2:
        msg_txt = "Hey! Can you please refill the beverage?"
    elif choice is 3:
        food_name = input("Please enter the food name: ")
        sauce_name = input("Please enter sauce if you want some (Enter None if you don't): ")
        micro_wave_time = input("Please enter time you want to give the food in microwave: ")

        msg_txt = "Hey! I wanna have some food. " + \
                  "\nFood: " + food_name + \
                  "\nSauce: " + sauce_name + \
                  "\nMicro Wave Time: " + micro_wave_time

    elif choice is 4:
        msg_txt = "Hey! I need my pills. Can you please bring them over?"
    elif choice is 5:
        msg_txt = "Hey! Can you please help me out with groceries?"
    elif choice is 6:
        item_name = input("Please Enter item name you want him to bring: ")
        msg_txt = "Hey! Can you please bring " + item_name + " for me?"
    elif choice is 7:
        msg_txt = "Hey! Can you please help your wife with Amin today?"
    elif choice is 8:
        msg_txt = "Hey! Can you please perform a professional massage? I'd really love to have one."
    elif choice is 9:
        msg_txt = "Hey! Can you please come? I need to talk to you."
    elif choice is 10:
        custom_message = input("Please enter your customized message: ")
        msg_txt = custom_message
    elif choice is 11:
        print("Good Bye :)")
        exit()

    msg_txt = msg_txt + msg_ending

    print("\nSending Notification. Please wait...")
    MailController().send_mail(msg_txt, from_email, from_pass, to_email)
    print("\n --------------------- \n\n")
