# import time
# import pyttsx3
# from win10toast import ToastNotifier
# toast = ToastNotifier()
# engine=pyttsx3.init()
# text=["sudhanshu kumar singh"]
# while True:
#     time.sleep(5)
#     toast.show_toast(
#     "Notification",
#     "please drink water sir",
#     duration=20,
#     icon_path="water.ico",
#     threaded=True,
#      )
#     engine.say(f"please Drink water {text}")
#     print("please drink water")
#     engine.runAndWait()



# It imports the ToastNotifier class from the win10toast module. This class is responsible for creating and displaying the notifications.
# It creates an instance of the ToastNotifier class and assigns it to the variable toast.
# It calls the show_toast method of the toast object, which takes the following parameters:
# title: The title of the notification, which is “Notification” in this case.
# message:    The message of the notification, which is “Notification body” in this case.
# duration:   The duration of the notification in seconds, which is 20 in this case.
#             This means the notification will disappear after 20 seconds, unless the user clicks on it.
# icon_path:  The path to the icon file that will be displayed on the notification, which is “icon.ico” in this case.
#             This file should be in the same folder as the Python script, or you can provide the full path to the file.
# threaded:   A boolean value that indicates whether the notification should be displayed in a separate thread or not, which is True in this case.
#             This means the notification will not block the execution of the rest of the code, and the user can interact with it.

   

# from win10toast import ToastNotifier
# toast = ToastNotifier()
# toast.show_toast(
#     "Notification",
#     "Notification body",
#     duration=20,
#     icon_path="icon.ico",
#     threaded=True,
# )




from plyer import notification
import pyttsx3
import time
while True:
    # initialize the speech engine
    engine = pyttsx3.init()
    time.sleep(5)
    # create a function that sends a notification and speaks the message
    def notify_and_speak(title, message):
        # send the notification
        notification.notify(
            title="notification",
            message="PLEASE DRINK WATER SIR",
            timeout=10,
        )
        # speak the message
        engine.say(message)
        engine.runAndWait()

    # test the function
    notify_and_speak("Hello, Python!", "PLEASE DRINK WATER SIR.")

