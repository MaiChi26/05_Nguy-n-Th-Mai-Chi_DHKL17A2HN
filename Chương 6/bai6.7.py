import threading
import time
from datetime import datetime

def google():
    print("Starting Google")
    for _ in range(5):
        now = datetime.now().strftime("%b %d %H:%M:%S %Y")
        print(f"Google: Web {now}")
        time.sleep(1)  
    print("Exiting Google")

def yahoo():
    print("Starting Yahoo")
    for _ in range(5):
        now = datetime.now().strftime("%b %d %H:%M:%S %Y")
        print(f"Yahoo: Web {now}")
        time.sleep(2)  
    print("Exiting Yahoo")

def facebook():
    print("Starting Facebook")
    for _ in range(5):
        now = datetime.now().strftime("%b %d %H:%M:%S %Y")
        print(f"Facebook: Web {now}")
        time.sleep(3)  
    print("Exiting Facebook")

if __name__ == "__main__":
    print("Starting Main Thread")

    luong_google = threading.Thread(target=google)
    luong_yahoo = threading.Thread(target=yahoo)
    luong_facebook = threading.Thread(target=facebook)

    luong_google.start()
    luong_yahoo.start()
    luong_facebook.start()

    luong_google.join()
    luong_yahoo.join()
    luong_facebook.join()

    print("Exiting Main Thread")
