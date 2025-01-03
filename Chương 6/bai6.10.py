import threading
import random

def tim_max_phan(danh_sach, ket_qua, chi_so):
    max_value = max(danh_sach)
    print(f"Thread {chi_so + 1}: {', '.join(map(str, danh_sach))} -> Max: {max_value}")
    ket_qua[chi_so] = max_value

def main():
    so_phan_tu = int(input("Nhập số phần tử trong danh sách: "))
    so_thread = int(input("Nhập số thread: "))

    danh_sach = [random.randint(0, 100) for _ in range(so_phan_tu)]
    print(f"List: {danh_sach}")

    buoc = so_phan_tu // so_thread
    cac_phan = [danh_sach[i * buoc: (i + 1) * buoc] for i in range(so_thread - 1)]
    cac_phan.append(danh_sach[(so_thread - 1) * buoc:])  

    ket_qua = [0] * so_thread
    cac_luong = []
    for i in range(so_thread):
        luong = threading.Thread(target=tim_max_phan, args=(cac_phan[i], ket_qua, i))
        cac_luong.append(luong)
        luong.start()

    for luong in cac_luong:
        luong.join()

    max_cuoi_cung = max(ket_qua)
    print(f"Giá trị lớn nhất trong list: {max_cuoi_cung}")

if __name__ == "__main__":
    main()
