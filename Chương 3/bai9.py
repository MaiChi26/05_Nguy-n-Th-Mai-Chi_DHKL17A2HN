import pandas as pd

# Tạo DataFrame euro12 từ file dữ liệu euro2012.csv
euro12 = pd.read_csv('euro2012.csv')

# In thông tin về DataFrame
print("Thông tin về kiểu dữ liệu:")
print(type(euro12))  # Kiểu dữ liệu của euro12

print("\nKích thước (shape) của DataFrame:", euro12.shape)

print("\nDanh sách các cột:")
print(euro12.columns)

# 1. In giá trị của cột 'Goals'
print("\nGiá trị cột 'Goals':")
print(euro12['Goals'])

# 2. Có bao nhiêu đội tham gia Euro 2012?
num_teams = euro12['Team'].nunique()  # Số lượng đội khác nhau
print("\nSố đội tham gia Euro 2012:", num_teams)

# 3. In thông tin tổng quát về DataFrame
print("\nThông tin tổng quát của Euro 2012:")
print(euro12.info())

# 4. Tạo DataFrame mới từ euro12 chỉ chứa các cột 'Team', 'Yellow Cards', 'Red Cards'
discipline = euro12[['Team', 'Yellow Cards', 'Red Cards']]
print("\nDataFrame discipline:\n", discipline)

# 5. Sắp xếp discipline giảm dần theo 2 cột 'Red Cards' và 'Yellow Cards'
discipline_sorted = discipline.sort_values(by=['Red Cards', 'Yellow Cards'], ascending=[False, False])
print("\nDiscipline được sắp xếp theo Red Cards và Yellow Cards:\n", discipline_sorted)

# 6a. Tính trung bình số thẻ vàng (Yellow Cards)
yellow_cards_avg = euro12['Yellow Cards'].mean()
print("\nTrung bình số thẻ vàng:", yellow_cards_avg)

# 6b. Lọc các đội đã ghi hơn 6 bàn thắng
teams_more_than_6_goals = euro12[euro12['Goals'] > 6]
print("\nCác đội ghi hơn 6 bàn thắng:\n", teams_more_than_6_goals[['Team', 'Goals']])

# 7. In các đội mà tên bắt đầu bằng 'G'
teams_start_with_G = euro12[euro12['Team'].str.startswith('G')]
print("\nCác đội có tên bắt đầu bằng 'G':\n", teams_start_with_G[['Team']])

# 8. In 7 cột đầu của euro12
print("\n7 cột đầu của DataFrame:\n", euro12.iloc[:, :7])

# 9. In tất cả các cột trừ 3 cột cuối
print("\nTất cả các cột trừ 3 cột cuối:\n", euro12.iloc[:, :-3])

# 10. In các cột 'Team', 'Goals', 'Shooting Accuracy', 'Yellow Cards', 'Red Cards'
print("\nCác cột 'Team', 'Goals', 'Shooting Accuracy', 'Yellow Cards', 'Red Cards':\n", 
      euro12[['Team', 'Goals', 'Shooting Accuracy', 'Yellow Cards', 'Red Cards']])

# 11. In các cột 'Team', 'Shooting Accuracy' từ các đội 'England', 'Italy', 'Russia'
teams_selected = euro12[euro12['Team'].isin(['England', 'Italy', 'Russia'])]
print("\nShooting Accuracy của các đội England, Italy, Russia:\n", 
      teams_selected[['Team', 'Shooting Accuracy']])
