import json

data_json = '''
{
    "company": {
        "name": "Công ty TNHH Đất Việt",
        "address": "abc Giải Phóng,Hà Nội",
        "employees": [
            {"name": "Nguyễn Văn A", "unit": "Đơn vị A1"},
            {"name": "Trần Thị B", "unit": "Đơn vị A1"},
            {"name": "Lê Văn C", "unit": "Đơn vị A2"},
            {"name": "Phạm Văn D", "unit": "Đơn vị A3"},
            {"name": "Nguyễn Văn E", "unit": "Đơn vị A4"},
            {"name": "Trần Thị F", "unit": "Đơn vị A4"},
            {"name": "Lê Văn G", "unit": "Đơn vị A4"}
        ]
    }
}
'''

# Chuyển đổi dữ liệu JSON thành đối tượng Python
du_lieu = json.loads(data_json)

# Lấy thông tin công ty
cong_ty = du_lieu['company']
ten_cong_ty = cong_ty['name']
dia_chi = cong_ty['address']
nhan_vien = cong_ty['employees']

# Thống kê tổng số nhân viên
tong_so_nhan_vien = len(nhan_vien)

# Thống kê số nhân viên theo đơn vị
thong_ke_don_vi = {}
for nhan_vien in nhan_vien:
    don_vi = nhan_vien['unit']
    if don_vi not in thong_ke_don_vi:
        thong_ke_don_vi[don_vi] = 0
    thong_ke_don_vi[don_vi] += 1

# In kết quả thống kê
print(f"Tên công ty: {ten_cong_ty}")
print(f"Địa chỉ: {dia_chi}")
print("-----Thống kê nhân viên theo đơn vị------")
for idx, (don_vi, so_nhan_vien) in enumerate(thong_ke_don_vi.items(), start=1):
    ty_le = (so_nhan_vien / tong_so_nhan_vien) * 100
    print(f"{idx}./Tên đơn vị: {don_vi}.")
    print(f"- Số nhân viên: {so_nhan_vien}.")
    print(f"- Tỷ lệ: {ty_le:.2f}%.")
