import threading
import requests

def thuc_hien_yeu_cau(url):
    try:
        phan_hoi = requests.get(url)
        print(f"URL: {url} - Mã trạng thái: {phan_hoi.status_code}")
    except Exception as e:
        print(f"Lỗi khi truy cập {url}: {e}")

cac_url = [
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/posts/2",
    "https://jsonplaceholder.typicode.com/posts/3",
    "https://jsonplaceholder.typicode.com/posts/4"
]

cac_luong = []

for url in cac_url:
    luong = threading.Thread(target=thuc_hien_yeu_cau, args=(url,))
    cac_luong.append(luong)
    luong.start()

for luong in cac_luong:
    luong.join()

print("Tất cả yêu cầu HTTP đã hoàn thành.")
