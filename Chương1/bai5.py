class Stack:
    def __init__(self):
        self.items = []  # Khởi tạo ngăn xếp rỗng

    def is_empty(self):
        return len(self.items) == 0  # Kiểm tra ngăn xếp có rỗng không

    def push(self, item):
        self.items.append(item)  # Thêm phần tử vào ngăn xếp

    def pop(self):
        if not self.is_empty():
            return self.items.pop()  # Lấy phần tử trên cùng ra khỏi ngăn xếp
        else:
            return "Ngăn xếp rỗng"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]  # Trả về phần tử trên cùng mà không lấy ra
        else:
            return "Ngăn xếp rỗng"

    def count(self):
        return len(self.items)  # Trả về số phần tử trong ngăn xếp

    def display(self):
        if not self.is_empty():
            print("Ngăn xếp:", self.items)  # Hiển thị ngăn xếp
        else:
            print("Ngăn xếp rỗng")

# Ví dụ sử dụng lớp Stack
def main():
    stack = Stack()
    
    # Thêm phần tử vào ngăn xếp
    stack.push(10)
    stack.push(20)
    stack.push(30)

    # Hiển thị ngăn xếp và số phần tử
    stack.display()
    print("Số phần tử trong ngăn xếp:", stack.count())

    # Lấy phần tử ra khỏi ngăn xếp
    stack.pop()
    stack.display()
    print("Số phần tử trong ngăn xếp:", stack.count())

if __name__ == "__main__":
    main()
