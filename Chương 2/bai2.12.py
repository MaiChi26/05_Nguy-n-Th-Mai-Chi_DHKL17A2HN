import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

if response.status_code == 200:
    danh_sach_bai_post = response.json()
    print(f"Tổng số bài post: {len(danh_sach_bai_post)}")
    print("\nDanh sách các bài post:")
    
    for post in danh_sach_bai_post:
        user_id = post['userId']
        post_id = post['id']
        title = post['title']
        body = post['body']
        
        print(f"UserID: {user_id}, ID: {post_id}, Tiêu đề: {title}, Nội dung: {body}\n")
else:
    print(f"Có lỗi xảy ra khi lấy dữ liệu từ API: {response.status_code}")
