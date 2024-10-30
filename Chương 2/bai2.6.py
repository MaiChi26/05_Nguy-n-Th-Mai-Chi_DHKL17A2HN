import requests
from xml.dom import minidom
import csv

# URL của RSS feed
rss_url = "http://www.hindustantimes.com/rss/topnews/rssfeed.xml"

# Bước 1: Tải RSS feed từ URL và lưu thành tệp XML
response = requests.get(rss_url)
with open("rssfeed.xml", "wb") as file:
    file.write(response.content)

# Bước 2: Phân tích cú pháp tệp XML để lấy các mục tin tức
# Tải file XML đã lưu
doc = minidom.parse("rssfeed.xml")

# Tạo danh sách các phần tử <item> chứa tin tức
items = doc.getElementsByTagName("item")

# Tạo danh sách để lưu tin tức dưới dạng từ điển
news_list = []

# Duyệt qua các mục tin tức
for item in items:
    title = item.getElementsByTagName("title")[0].firstChild.data
    link = item.getElementsByTagName("link")[0].firstChild.data
    description = item.getElementsByTagName("description")[0].firstChild.data
    pub_date = item.getElementsByTagName("pubDate")[0].firstChild.data
    
    # Tạo từ điển lưu từng mục tin tức
    news = {
        "Title": title,
        "Link": link,
        "Description": description,
        "Publication Date": pub_date
    }
    
    # Thêm vào danh sách tin tức
    news_list.append(news)

# Bước 3: Lưu các mục tin tức vào tệp CSV
with open("news.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["Title", "Link", "Description", "Publication Date"])
    writer.writeheader()
    
    # Ghi từng tin tức vào tệp CSV
    for news in news_list:
        writer.writerow(news)

print("RSS feed đã được lưu thành công vào news.csv!")
