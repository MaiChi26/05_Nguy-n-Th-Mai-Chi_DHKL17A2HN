class Hinh_Chu_Nhat:    #Tạo 1 lớp, đại diện cho hình chữ nhật
    def __init__(self, length, width):   # hàm khởi tạo ()
        self.length = length     #gắn các thuộc tính cho self
        self.width = width

    def dien_tich_hcn(self):    #Định nghĩa để tính S hnhat
        return self.length * self.width

    def chu_vi_hcn(self):
        return 2 * (self.length + self.width)

Hinh_Chu_Nhat = Hinh_Chu_Nhat(8, 4) #Tạo 1 lớp đối tượng mới từ lớp HCN
dientich = Hinh_Chu_Nhat.dien_tich_hcn()  #Gọi phương thức diện tích hình chữ nhật để tính diện tích hcn và gán kết quả cho biến
chuvi = Hinh_Chu_Nhat.chu_vi_hcn() 

print("Độ dài 2 cạnh của hình chữ nhật lần lượt là: ", Hinh_Chu_Nhat.length, Hinh_Chu_Nhat.width)
print("Diện tích của hình chữ nhật là:", dientich)
print("Chu vi của hình chữ nhật là:", chuvi)