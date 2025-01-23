import json
from apple_app_reviews_scraper import get_token, fetch_reviews

user_agents = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.4 Safari/605.1.15',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
]

country = 'jp'
app_name = 'sana' # can be named anything, really
app_id = '1597898870'

# Get token
token = get_token(country, app_name, app_id, user_agents)

print(f"Authentication Token: {token}")

all = []
offsetStart = '1'

while True:
  reviews, offset, status_code = fetch_reviews(country, app_name, app_id, user_agents, token, offset=offsetStart)
  offsetStart = offset
  all.extend(reviews)
  if len(reviews) < 20:
    break

stringO = json.dumps(all, indent=2, ensure_ascii=False, default=str)

with open("out.txt", "w", encoding='utf-8') as text_file:
    text_file.write(stringO)

print(len(all))
