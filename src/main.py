import json
from apple_app_reviews_scraper import get_token, fetch_reviews

user_agents = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.4 Safari/605.1.15',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
]

country = 'jp'
app_name = 'サンエー' # can be named anything, really
app_id = '1597898870'

# Get token
token = get_token(country, app_name, app_id, user_agents)

print(f"Authentication Token: {token}")

reviews, offset, status_code = fetch_reviews(country, app_name, app_id, user_agents, token)

stringO = json.dumps(reviews, indent=2, ensure_ascii=False, default=str)
print(stringO)
with open("out.txt", "w", encoding='utf-8') as text_file:
    text_file.write(stringO)

print(len(reviews))
