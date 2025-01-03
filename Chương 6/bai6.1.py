import threading

# Hàm để in tên của luồng
def in_ten_luong():
    print(f"Tên luồng hiện tại: {threading.current_thread().name}")

# Tạo danh sách các luồng
so_luong_luong = 5
cac_luong = []

for i in range(so_luong_luong):
    # Đặt tên cho luồng
    ten_luong = f"Luồng-{i+1}"
    luong = threading.Thread(target=in_ten_luong, name=ten_luong)
    cac_luong.append(luong)

# Bắt đầu các luồng
for luong in cac_luong:
    luong.start()

# Đảm bảo tất cả luồng hoàn thành
for luong in cac_luong:
    luong.join()

print("Hoàn tất!")
