import json

# Đối tượng từ điển Python
data= {
    "ten": "Mai Chi",
    "tuoi": 19,
    "thanh_pho": "VIETNAM",
    "so_thich ": ["doc_sach", "di_du_lich", "chup_anh"]
}

json_data = json.dumps(data, indent=4, sort_keys=True)

# In chuỗi JSON ra màn hình
print(json_data)
