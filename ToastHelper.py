from win10toast import ToastNotifier

def ShowToastMessage(message):
    toastMessage = ToastNotifier()
    toastMessage.show_toast(
        "Heyy, Today is race day :)",
        "{} don't miss the race. Watch the race bro!".format(message),
        icon_path="f1.ico",
        duration=20,
    )

