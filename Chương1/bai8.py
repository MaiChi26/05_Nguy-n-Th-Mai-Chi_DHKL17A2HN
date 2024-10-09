# Giả sử đã có lớp Date như trong bài 7
class Date:
    def __init__(self, day=1, month=1, year=2000):
        self.day = day
        self.month = month
        self.year = year

    def display(self):
        print(f"{self.day:02}/{self.month:02}/{self.year}")
    
    # Phương thức tính năm nhuận
    def is_leap_year(self):
        return (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)

    def days_in_month(self):
        if self.month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif self.month in [4, 6, 9, 11]:
            return 30
        elif self.month == 2:
            return 29 if self.is_leap_year() else 28

    def next(self):
        if self.day < self.days_in_month():
            self.day += 1
        else:
            self.day = 1
            if self.month < 12:
                self.month += 1
            else:
                self.month = 1
                self.year += 1

# Lớp Employee
class Nhan_vien:
    def __init__(self, name, birth_date, hire_date, position, salary):
        self.name = name  # Họ tên nhân viên
        self.birth_date = birth_date  # Ngày sinh kiểu Date
        self.hire_date = hire_date  # Ngày vào công ty kiểu Date
        self.position = position  # Vị trí công việc
        self.salary = salary  # Lương

    # Phương thức hiển thị thông tin nhân viên
    def display(self):
        print(f"Tên nhân viên: {self.name}")
        print("Ngày sinh:", end=" ")
        self.birth_date.display()
        print("Ngày vào công ty:", end=" ")
        self.hire_date.display()
        print(f"Vị trí: {self.position}")
        print(f"Lương: {self.salary} VND")

# Ví dụ sử dụng
# Tạo ngày sinh và ngày vào công ty
birth_date = Date(15, 8, 1990)
hire_date = Date(1, 5, 2020)

# Tạo một nhân viên
Nhan_vien = Nhan_vien("Nguyễn Văn A", birth_date, hire_date, "Kỹ sư phần mềm", 15000000)

# Hiển thị thông tin nhân viên
Nhan_vien.display()
