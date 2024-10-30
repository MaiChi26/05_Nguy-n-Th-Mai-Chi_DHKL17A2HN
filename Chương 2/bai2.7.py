import json

# Chuỗi JSON chứa danh sách màu
json_data = '["red", "yellow","blue"]'

# Chuyển đổi chuỗi JSON thành đối tượng Python
python_obj = json.loads(json_data)

# In đối tượng Python đã chuyển đổi
print("Đối tượng Python:", python_obj)

# In ra từng màu trong danh sách
for color in python_obj:
    print("Màu:", color)
