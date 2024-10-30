import json

news_list = ["red", "yellow"]

json_data = json.dumps(news_list)

print(json_data)

for item in news_list:
    print(item)
