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

def main():
    print("Starting Main Thread")

    thread_google = threading.Thread(target=google)
    thread_yahoo = threading.Thread(target=yahoo)
    thread_facebook = threading.Thread(target=facebook)

    thread_google.start()
    thread_yahoo.start()
    thread_facebook.start()

    thread_google.join()
    thread_yahoo.join()
    thread_facebook.join()

    print("Exiting Main Thread")

if __name__ == "__main__":
    main()
