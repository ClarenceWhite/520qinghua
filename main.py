from datetime import datetime
import time
from send_msg import Msg

if __name__ == '__main__':
    #create a class instance
    send_msg = Msg()

    while True:
        now = datetime.now()
        print("From main.py, now is:", now)
        minute = now.minute
        try:
            #run every 59 minutes
            if (minute % 59 == 0):
                print("From main.py, start sending qinghua......")
                send_msg.send_message()
                print("From main.py, end sending qinghua......")
                time.sleep(120)
        except Exception as e:
            print("Error in main.py:", e)


