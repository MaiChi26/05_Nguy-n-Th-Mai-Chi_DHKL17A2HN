class PhanSo:
    def __init__(self, tu_so, mau_so):
        self.tu_so = tu_so
        self.mau_so = mau_so

    def kiem_tra_hop_le(self):
        return self.mau_so != 0

    def nhap_phan_so(self):
        self.tu_so = int(input("Nhập tử số: "))
        self.mau_so = int(input("Nhập mẫu số: "))
        while not self.kiem_tra_hop_le():
            print("Mẫu số phải khác 0. Vui lòng nhập lại!")
            self.mau_so = int(input("Nhập mẫu số: "))

    def in_phan_so(self):
        print(f"{self.tu_so}/{self.mau_so}")
        
    # Tạo đối tượng PhanSo
phan_so = PhanSo(0, 1)

# Nhập phân số từ bàn phím
phan_so.nhap_phan_so()

# In phân số ra màn hình
phan_so.in_phan_so()

