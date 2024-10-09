import math

# Lớp Đa giác
class Polygon:
    def __init__(self, sides):
        self.sides = sides  # Danh sách chiều dài các cạnh

    def perimeter(self):
        return sum(self.sides)  # Tính chu vi bằng tổng chiều dài các cạnh

# Lớp Hình bình hành kế thừa từ Đa giác
class Hinh_binh_hanh(Polygon):
    def __init__(self, base, side, height):
        super().__init__([base, side, base, side])  # Gọi hàm khởi tạo của Polygon với 4 cạnh
        self.base = base
        self.side = side
        self.height = height

    def area(self):
        return self.base * self.height  # Diện tích = đáy * chiều cao

# Lớp Hình chữ nhật kế thừa từ Hình bình hành
class Hinh_chu_nhat(Hinh_binh_hanh):
    def __init__(self, length, width):
        super().__init__(length, width, width)  # Chiều cao trong Hình chữ nhật là độ dài của chiều rộng
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width  # Diện tích = dài * rộng

# Lớp Hình vuông kế thừa từ Hình chữ nhật
class Hinh_vuong(Hinh_chu_nhat):
    def __init__(self, side):
        super().__init__(side, side)  # Cạnh dài và cạnh rộng đều bằng cạnh của hình vuông
        self.side = side

    def area(self):
        return self.side ** 2  # Diện tích = cạnh^2

# Ví dụ sử dụng chương trình
def main():
    # Nhập thông tin cho Hình bình hành
    print("Nhập thông tin Hình bình hành:")
    base = float(input("Đáy: "))
    side = float(input("Cạnh bên: "))
    height = float(input("Chiều cao: "))
    parallelogram = Hinh_binh_hanh(base, side, height)
    print(f"Chu vi hình bình hành: {parallelogram.perimeter()}")
    print(f"Diện tích hình bình hành: {parallelogram.area()}")

    # Nhập thông tin cho Hình chữ nhật
    print("\nNhập thông tin Hình chữ nhật:")
    length = float(input("Chiều dài: "))
    width = float(input("Chiều rộng: "))
    rectangle = Hinh_chu_nhat(length, width)
    print(f"Chu vi hình chữ nhật: {rectangle.perimeter()}")
    print(f"Diện tích hình chữ nhật: {rectangle.area()}")

    # Nhập thông tin cho Hình vuông
    print("\nNhập thông tin Hình vuông:")
    side = float(input("Cạnh: "))
    square = Hinh_vuong(side)
    print(f"Chu vi hình vuông: {square.perimeter()}")
    print(f"Diện tích hình vuông: {square.area()}")

# Chạy chương trình
if __name__ == "__main__":
    main()
