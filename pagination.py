import requests

r = requests.get('https://quotes.toscrape.com/')
print(r.status_code)
html = r.text