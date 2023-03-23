import requests
from email_config import send_email

api_key = 'c5277bbf8a444cbabab89db5e6b4fd47'
url = 'https://newsapi.org/v2/everything?q=apple&from=2023-03-22&to=2023-03-22&sortBy=popularity&apiKey=c5277bbf8a444cbabab89db5e6b4fd47'

request = requests.get(url)
content = request.json()

message_body = ''
for article in content['articles']:
    message_body = message_body + article['title'] + '\n' + article['description'] + 2*'\n'

send_email(message_body)