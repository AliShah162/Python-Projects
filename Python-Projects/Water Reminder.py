import  time
from plyer import notification

if __name__=="__main__":
    while(True):
        notification.notify(
        title="***Please Drink Water***",
        message="You Need 3.7 Liters a Day!",
        timeout=5
    )
        time.sleep(3)  