import requests

url = "https://jsonplaceholder.typicode.com/comments?postId=1"

response = requests.get(url)

if response.status_code == 200:
    danh_sach_binh_luan = response.json()
    print("Danh sách các bài post nổi bật:")
    
    for i, binh_luan in enumerate(danh_sach_binh_luan):
        if i >= 3:  
            break
        
        post_id = binh_luan['postId']
        comment_id = binh_luan['id']
        name = binh_luan['name']
        email = binh_luan['email']
        body = binh_luan['body']
        
        print(f"Bài post ID: {post_id}, Bình luận ID: {comment_id}, Tên: {name}, Email: {email}, Nội dung: {body}\n")
else:
    print(f"Có lỗi xảy ra khi lấy dữ liệu từ API: {response.status_code}")
