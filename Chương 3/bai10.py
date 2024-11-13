import pandas as pd

# 1. Đọc dữ liệu từ tệp drinks.csv, sử dụng cột đầu tiên làm index
drink = pd.read_csv('drinks.csv')

# 1a. Hiển thị kiểu dữ liệu và kích thước của DataFrame
print("Kiểu dữ liệu của drink:", type(drink))
print("Kích thước của drink (số dòng, số cột):", drink.shape)

# 1b. Hiển thị tên các cột
print("\nTên các cột trong drink:")
print(drink.columns)

# 1c. Xem 5 dòng đầu tiên và 5 dòng cuối cùng của DataFrame
print("\n5 dòng đầu tiên của drink:")
print(drink.head())

print("\n5 dòng cuối cùng của drink:")
print(drink.tail())

# 2. Cho biết số lượng bia tiêu thụ trung bình ở mỗi châu lục
avg_beer_per_continent = drink.groupby('continent')['beer_servings'].mean()
print("\nSố lượng bia tiêu thụ trung bình ở mỗi châu lục:")
print(avg_beer_per_continent)

# 3. Thống kê tổng quát (describe) số lượng rượu vang được tiêu thụ ở mỗi châu lục
wine_stats_per_continent = drink.groupby('continent')['wine_servings'].describe()
print("\nThống kê tổng quát số lượng rượu vang được tiêu thụ ở mỗi châu lục:")
print(wine_stats_per_continent)

# 4. Tính trung bình số lượng bia và rượu tiêu thụ ở mỗi châu lục
avg_beer_wine_per_continent = drink.groupby('continent')[['beer_servings', 'wine_servings']].mean()
print("\nSố lượng bia và rượu tiêu thụ trung bình ở mỗi châu lục:")
print(avg_beer_wine_per_continent)

# 5. Tính giá trị trung vị (median) của bia và rượu tiêu thụ ở mỗi châu lục
median_beer_wine_per_continent = drink.groupby('continent')[['beer_servings', 'wine_servings']].median()
print("\nGiá trị trung vị của bia và rượu tiêu thụ ở mỗi châu lục:")
print(median_beer_wine_per_continent)

# 6. Thống kê số lượng spirit servings (rượu mạnh) tiêu thụ trung bình, lớn nhất và nhỏ nhất ở mỗi châu lục
spirit_stats_per_continent = drink.groupby('continent')['spirit_servings'].agg(['mean', 'max', 'min'])
print("\nThống kê số lượng rượu mạnh tiêu thụ trung bình, lớn nhất và nhỏ nhất ở mỗi châu lục:")
print(spirit_stats_per_continent)

# 7. Sắp xếp dữ liệu tăng dần theo số lượng bia tiêu thụ
sorted_by_beer = drink.sort_values(by='beer_servings')

# 7a. 5 quốc gia có lượng tiêu thụ bia nhiều nhất
top_5_beer_countries = sorted_by_beer.tail(5)
print("\n5 quốc gia có lượng tiêu thụ bia nhiều nhất:")
print(top_5_beer_countries[['beer_servings']])

# 7b. 5 quốc gia có lượng tiêu thụ bia ít nhất
bottom_5_beer_countries = sorted_by_beer.head(5)
print("\n5 quốc gia có lượng tiêu thụ bia ít nhất:")
print(bottom_5_beer_countries[['beer_servings']])
