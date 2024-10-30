from xml.dom import minidom

# Tải và phân tích file XML
doc = minidom.parse("sample.xml")

# Sử dụng phương thức getElementsByTagName() để lấy tất cả các phần tử <staff>
staff_list = doc.getElementsByTagName("staff")

# Duyệt qua danh sách các phần tử và in tên của từng phần tử
for staff in staff_list:
    name = staff.getElementsByTagName("name")[0].firstChild.data
    salary = staff.getElementsByTagName("salary")[0].firstChild.data
    print(f"Name: {name}, Salary: {salary}")
