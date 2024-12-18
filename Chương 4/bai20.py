import pandas as pd

du_lieu_euro2012 = pd.read_csv('euro2012.csv')

print("Kiểu dữ liệu:", type(du_lieu_euro2012))
print("Hình dạng:", du_lieu_euro2012.shape)
print("Danh sách các cột:", du_lieu_euro2012.columns)

# 1. 
print(du_lieu_euro2012['Goals'])

# 2. 
print("Số đội tham gia Euro 2012:", du_lieu_euro2012['Team'].nunique())

# 3. 
print(du_lieu_euro2012)

# 4. 
khen_thuong_ky_luat = du_lieu_euro2012[['Team', 'Yellow Cards', 'Red Cards']]
print(khen_thuong_ky_luat)

# 5.
khen_thuong_ky_luat_sorted = khen_thuong_ky_luat.sort_values(by=['Red Cards', 'Yellow Cards'], ascending=False)
print(khen_thuong_ky_luat_sorted)

# 6a) 
print("Trung bình Yellow Cards:", du_lieu_euro2012['Yellow Cards'].mean())

# b) 
doi_hon_6_ban_thang = du_lieu_euro2012[du_lieu_euro2012['Goals'] > 6]
print(doi_hon_6_ban_thang)

# 7. 
doi_bat_dau_bang_G = du_lieu_euro2012[du_lieu_euro2012['Team'].str.startswith('G')]
print(doi_bat_dau_bang_G)

# 8. 
print(du_lieu_euro2012.iloc[:, :7])

# 9. 
print(du_lieu_euro2012.iloc[:, :-3])

# 10. 
print(du_lieu_euro2012[['Team', 'Goals', 'Shooting Accuracy', 'Yellow Cards', 'Red Cards']])

# 11.
doi_lieu_quan_tam = du_lieu_euro2012[du_lieu_euro2012['Team'].isin(['England', 'Italy', 'Russia'])][['Team', 'Shooting Accuracy']]
print(doi_lieu_quan_tam)
