import pandas as pd

# Dữ liệu đầu vào
emails = pd.Series(['buying books at amazom.com', 'rameses@egypt.com', 'mattigt.co.', 'narendra@modi.com'])

pattern = r"[A-Za-z0-9_%+-]+@[A-Za-z0-9-]+\.[A-Za-z]{2,41}"
valid_emails = emails[emails.str.contains(pattern, regex=True)]

print(valid_emails)
