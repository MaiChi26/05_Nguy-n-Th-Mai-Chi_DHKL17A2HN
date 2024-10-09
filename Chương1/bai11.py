import math 

# Lớp Tam Giác
class Tam_giac:
    def __init__(self, a, b, c):
        self.a = a  # Cạnh 1
        self.b = b  # Cạnh 2
        self.c = c  # Cạnh 3

    def area(self):
        # Sử dụng công thức Heron để tính diện tích
        s = (self.a + self.b + self.c) / 2  # Nửa chu vi
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))  # Diện tích

# Lớp Tam Giác Vuông kế thừa từ lớp Tam Giác
class Tam_giac_vuong(Tam_giac):
    def __init__(self, base, height):
        self.base = base  # Cạnh đáy
        self.height = height  # Chiều cao
        # Cạnh huyền
        self.hypotenuse = math.sqrt(base**2 + height**2)
        super().__init__(base, height, self.hypotenuse)

    def area(self):
        return (self.base * self.height) / 2  # Diện tích = 1/2 * đáy * chiều cao

# Lớp Tam Giác Cân kế thừa từ lớp Tam Giác
class Tam_giac_can(Tam_giac):
    def __init__(self, base, side):
        self.base = base  # Cạnh đáy
        self.side = side  # Cạnh bên
        super().__init__(base, side, side)  # Cạnh bên bằng nhau

    def area(self):
        height = math.sqrt(self.side**2 - (self.base / 2)**2)  # Tính chiều cao
        return (self.base * height) / 2  # Diện tích = 1/2 * đáy * chiều cao

# Lớp Tam Giác Đều kế thừa từ lớp Tam Giác Cân
class Tam_giac_deu(Tam_giac_can):
    def __init__(self, side):
        super().__init__(side, side)  # Cạnh bên và đáy đều bằng nhau

    def area(self):
        return (math.sqrt(3) / 4) * self.base ** 2  # Diện tích = (√3/4) * a^2

# Ví dụ sử dụng cho bài 11
def main_triangle():
    print("Nhập thông tin Tam Giác:")
    a = float(input("Cạnh a: "))
    b = float(input("Cạnh b: "))
    c = float(input("Cạnh c: "))
    
    triangle = Tam_giac(a, b, c)
    print(f"Diện tích Tam Giác: {triangle.area()}")

    print("\nNhập thông tin Tam Giác Vuông:")
    base = float(input("Cạnh đáy: "))
    height = float(input("Chiều cao: "))
    
    right_triangle = Tam_giac_vuong(base, height)
    print(f"Diện tích Tam Giác Vuông: {right_triangle.area()}")

    print("\nNhập thông tin Tam Giác Cân:")
    base_isosceles = float(input("Cạnh đáy: "))
    side = float(input("Cạnh bên: "))
    
    isosceles_triangle = Tam_giac_can(base_isosceles, side)
    print(f"Diện tích Tam Giác Cân: {isosceles_triangle.area()}")

    print("\nNhập thông tin Tam Giác Đều:")
    side_equilateral = float(input("Cạnh: "))
    
    equilateral_triangle = Tam_giac_deu(side_equilateral)
    print(f"Diện tích Tam Giác Đều: {equilateral_triangle.area()}")

# Chạy chương trình bài 11
if __name__ == "__main__":
    main_triangle()
