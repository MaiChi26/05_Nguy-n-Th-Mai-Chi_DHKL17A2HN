import threading
import requests

# Hàm tải xuống một tệp
def tai_tap_tin(url, ten_tap_tin):
    try:
        print(f"Đang tải: {ten_tap_tin}")
        phan_hoi = requests.get(url)
        with open(ten_tap_tin, "wb") as tap_tin:
            tap_tin.write(phan_hoi.content)
        print(f"Hoàn tất: {ten_tap_tin}")
    except Exception as e:
        print(f"Lỗi khi tải {ten_tap_tin}: {e}")

# Danh sách URL và tên tệp tương ứng
tap_tin_can_tai = [
    {"url": "https://example.com/file1.jpg", "ten_tap_tin": "file1.jpg"},
    {"url": "https://example.com/file2.jpg", "ten_tap_tin": "file2.jpg"},
    {"url": "https://example.com/file3.jpg", "ten_tap_tin": "file3.jpg"}
]

# Tạo và khởi chạy luồng cho từng tệp
cac_luong = []

for tap_tin in tap_tin_can_tai:
    url = tap_tin["url"]
    ten_tap_tin = tap_tin["ten_tap_tin"]
    luong = threading.Thread(target=tai_tap_tin, args=(url, ten_tap_tin))
    cac_luong.append(luong)
    luong.start()

# Đợi tất cả các luồng hoàn thành
for luong in cac_luong:
    luong.join()

print("Tất cả các tệp đã được tải xuống.")
