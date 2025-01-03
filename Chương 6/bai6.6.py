import threading

nguong = 20

khoa = threading.Lock()
luot = 0  

def in_so_chan():
    global luot
    for i in range(0, nguong + 1, 2):
        with khoa:
            while luot != 0:  
                khoa.wait()
            print(f"Số chẵn: {i}")
            luot = 1  
            khoa.notify_all() 

def in_so_le():
    global luot
    for i in range(1, nguong + 1, 2):
        with khoa:
            while luot != 1:  
                khoa.wait()
            print(f"Số lẻ: {i}")
            luot = 0  
            khoa.notify_all()  

luong_chan = threading.Thread(target=in_so_chan)
luong_le = threading.Thread(target=in_so_le)

luong_chan.start()
luong_le.start()

luong_chan.join()
luong_le.join()

print("Hoàn tất!")
