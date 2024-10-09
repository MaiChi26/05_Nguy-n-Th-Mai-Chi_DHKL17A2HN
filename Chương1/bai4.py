class Stack:
    def __init__(self, capacity):
        self.capacity = capacity  # Dung lượng tối đa của ngăn xếp
        self.stack = []  # Mảng lưu các phần tử kiểu float
        self.top = -1  # Đỉnh của ngăn xếp, ban đầu chưa có phần tử nào
        
    def __del__(self):
        del self.stack  # Giải phóng bộ nhớ khi ngăn xếp không còn được sử dụng
    
    # Phương thức kiểm tra ngăn xếp có trống không
    def isEmpty(self):
        return self.top == -1
    
    # Phương thức kiểm tra ngăn xếp có đầy không
    def isFull(self):
        return self.top == self.capacity - 1
    
    # Phương thức thêm một phần tử vào đỉnh ngăn xếp
    def push(self, value):
        if self.isFull():
            print("Ngăn xếp đã đầy, không thể thêm phần tử!")
        else:
            self.stack.append(value)
            self.top += 1
            print(f"Đã thêm {value} vào ngăn xếp.")
    
    # Phương thức lấy một phần tử ra từ đỉnh ngăn xếp
    def pop(self):
        if self.isEmpty():
            print("Ngăn xếp trống, không thể lấy phần tử!")
            return None
        else:
            popped_value = self.stack.pop()
            self.top -= 1
            print(f"Đã lấy {popped_value} ra khỏi ngăn xếp.")
            return popped_value
    
    # Phương thức hiển thị ngăn xếp hiện tại
    def display(self):
        if self.isEmpty():
            print("Ngăn xếp trống.")
        else:
            print("Ngăn xếp hiện tại:", self.stack)

# Chương trình chính
def main():
    capacity = int(input("Nhập dung lượng của ngăn xếp: "))
    stack = Stack(capacity)
    
    while True:
        print("\nChọn thao tác:")
        print("1. Push (Thêm phần tử vào ngăn xếp)")
        print("2. Pop (Lấy phần tử ra khỏi ngăn xếp)")
        print("3. Kiểm tra ngăn xếp có trống không")
        print("4. Kiểm tra ngăn xếp có đầy không")
        print("5. Hiển thị ngăn xếp")
        print("6. Thoát")
        
        choice = int(input("Nhập lựa chọn của bạn: "))
        
        if choice == 1:
            value = float(input("Nhập giá trị cần thêm vào ngăn xếp: "))
            stack.push(value)
        elif choice == 2:
            stack.pop()
        elif choice == 3:
            if stack.isEmpty():
                print("Ngăn xếp trống.")
            else:
                print("Ngăn xếp không trống.")
        elif choice == 4:
            if stack.isFull():
                print("Ngăn xếp đầy.")
            else:
                print("Ngăn xếp chưa đầy.")
        elif choice == 5:
            stack.display()
        elif choice == 6:
            break
        else:
            print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()
