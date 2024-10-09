class Date:
    # Hàm tạo với các giá trị mặc định
    def __init__(self, day=1, month=1, year=2000):
        self.day = day
        self.month = month
        self.year = year

    # Phương thức kiểm tra năm nhuận
    def is_leap_year(self):
        return (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)

    # Phương thức trả về số ngày trong tháng
    def days_in_month(self):
        if self.month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif self.month in [4, 6, 9, 11]:
            return 30
        elif self.month == 2:
            return 29 if self.is_leap_year() else 28

    # Phương thức hiển thị thông tin ngày, tháng, năm
    def display(self):
        print(f"{self.day:02}/{self.month:02}/{self.year}")

    # Phương thức tính ngày tiếp theo
    def next(self):
        # Tính ngày tiếp theo
        if self.day < self.days_in_month():
            self.day += 1
        else:
            self.day = 1
            if self.month < 12:
                self.month += 1
            else:
                self.month = 1
                self.year += 1

print("ngày hôm nay là: ")
date = Date(31, 10, 2024)
date.display()  
print("ngày tiếp theo là: ")
date.next()
date.display()  

