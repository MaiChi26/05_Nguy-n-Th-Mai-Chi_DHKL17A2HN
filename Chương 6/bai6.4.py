import threading

ket_qua = 1
khoa = threading.Lock()

def tinh_tich(bat_dau, ket_thuc):
    global ket_qua
    tich_cuc_bo = 1
    for i in range(bat_dau, ket_thuc + 1):
        tich_cuc_bo *= i
    
    with khoa:
        ket_qua *= tich_cuc_bo

def tinh_giai_thua(so, so_luong_luong):
    buoc = so // so_luong_luong
    cac_luong = []
    
    for i in range(so_luong_luong):
        bat_dau = i * buoc + 1
        ket_thuc = (i + 1) * buoc if i < so_luong_luong - 1 else so
        luong = threading.Thread(target=tinh_tich, args=(bat_dau, ket_thuc))
        cac_luong.append(luong)
        luong.start()

    for luong in cac_luong:
        luong.join()

    return ket_qua

so = 10  # Giai thừa của 10
so_luong_luong = 3
print(f"Giai thừa của {so} là: {tinh_giai_thua(so, so_luong_luong)}")
