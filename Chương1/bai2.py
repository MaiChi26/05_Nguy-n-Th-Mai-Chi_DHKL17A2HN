
class Thi_sinh:    # khai báp một lớp để mô tả đối tượng  thí sinh
    def __init__(self, ho_ten, diem_toan, diem_ly, diem_hoa):    # hàm khởi tạo
        self.ho_ten = ho_ten
        self.diem_toan = diem_toan
        self.diem_ly = diem_ly
        self.diem_hoa = diem_hoa
    
    def tinh_tong_diem(self):
        return self.diem_toan + self.diem_ly + self.diem_hoa

    def in_thong_tin(self):
        print(f'Họ tên: {self.ho_ten}, Tổng điểm: {self.tinh_tong_diem()}')

def nhap_danh_sach_thi_sinh():
    danh_sach = []
    so_luong = int(input("Nhập số lượng thí sinh: "))
    for i in range(so_luong):
        ho_ten = input(f"Nhập họ tên thí sinh thứ {i+1}: ")
        diem_toan = float(input("Nhập điểm Toán: "))
        diem_ly = float(input("Nhập điểm Lý: "))
        diem_hoa = float(input("Nhập điểm Hoá: "))
        ts = Thi_sinh(ho_ten, diem_toan, diem_ly, diem_hoa)
        danh_sach.append(ts)
    return danh_sach

# In danh sách thí sinh trúng tuyển theo thứ tự điểm từ cao xuống thấp
def in_danh_sach_trung_tuyen(danh_sach):
    diem_chuan = 20
    
    # Lọc danh sách các thí sinh có tổng điểm >= điểm chuẩn
    danh_sach_trung_tuyen = [ts for ts in danh_sach if ts.tinh_tong_diem() >= diem_chuan]
    
    # Sắp xếp danh sách theo tổng điểm từ cao xuống thấp
    danh_sach_trung_tuyen.sort(key=lambda ts: ts.tinh_tong_diem(), reverse=True)
    print("\nDanh sách thí sinh trúng tuyển:")
    for ts in danh_sach_trung_tuyen:
        ts.in_thong_tin()

def main(): #Gọi các hàm nhập danh sách thí sinh và in danh sách thí sinh trúng tuyển.
    danh_sach = nhap_danh_sach_thi_sinh()
    in_danh_sach_trung_tuyen(danh_sach)

if __name__ == "__main__":
    main()
