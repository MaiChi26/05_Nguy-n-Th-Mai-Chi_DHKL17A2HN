import threading

def in_so_chan():
    print("Các số chẵn từ 30 đến 50:")
    for i in range(30, 51):
        if i % 2 == 0:
            print(f"Số chẵn: {i}")

def in_so_le():
    print("Các số lẻ từ 30 đến 50:")
    for i in range(30, 51):
        if i % 2 != 0:
            print(f"Số lẻ: {i}")

luong_chan = threading.Thread(target=in_so_chan)
luong_le = threading.Thread(target=in_so_le)

luong_chan.start()
luong_le.start()

luong_chan.join()
luong_le.join()

print("Hoàn tất!")
 