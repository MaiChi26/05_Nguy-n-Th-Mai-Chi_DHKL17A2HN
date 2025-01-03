import threading
import random

def tinh_tong_phan(danh_sach, ket_qua, chi_so):
    tong = sum(danh_sach)
    print(f"Thread {chi_so + 1}: {', '.join(map(str, danh_sach))}")
    ket_qua[chi_so] = tong

def main():
    so_phan_tu = int(input("Nhập số phần tử trong danh sách: "))
    so_thread = int(input("Nhập số thread: "))

    danh_sach = [random.randint(0, 10) for _ in range(so_phan_tu)]
    print(f"List: {danh_sach}")

    buoc = so_phan_tu // so_thread
    cac_phan = [danh_sach[i * buoc: (i + 1) * buoc] for i in range(so_thread - 1)]
    cac_phan.append(danh_sach[(so_thread - 1) * buoc:])  # Phần cuối cùng

    ket_qua = [0] * so_thread
    cac_luong = []
    for i in range(so_thread):
        luong = threading.Thread(target=tinh_tong_phan, args=(cac_phan[i], ket_qua, i))
        cac_luong.append(luong)
        luong.start()

    for luong in cac_luong:
        luong.join()

    tong_cuoi_cung = sum(ket_qua)
    print(f"Tổng list: {tong_cuoi_cung}")

if __name__ == "__main__":
    main()
