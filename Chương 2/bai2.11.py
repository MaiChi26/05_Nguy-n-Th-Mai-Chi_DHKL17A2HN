import json
from datetime import datetime

def ghi_giao_dich_vao_file(giao_dich_list):
    now = datetime.now()
    filename = now.strftime("%Y-%m-%d-%H-%M-%S") + ".json"

    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(giao_dich_list, file, ensure_ascii=False, indent=4)

    print(f"Giao dịch đã được ghi vào tệp: {filename}")

giao_dich_list = []

while True:
   
    loai_giao_dich = input("Nhập loại giao dịch (tiền hoặc vàng): ").strip().lower()
    so_tien = float(input("Nhập số tiền hoặc số vàng: "))

    giao_dich = {
        "loai": loai_giao_dich,
        "so": so_tien,
        "thoi_gian": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    giao_dich_list.append(giao_dich)

    tiep_tuc = input("Bạn có muốn tiếp tục thực hiện giao dịch không? (có/không): ").strip().lower()
    if tiep_tuc != "có":
        break

ghi_vao_file = input("Bạn có muốn ghi các giao dịch vào tệp không? (1: Có, 0: Không): ").strip()
if ghi_vao_file == "1":
    ghi_giao_dich_vao_file(giao_dich_list)
else:
    print("Không ghi giao dịch.")
