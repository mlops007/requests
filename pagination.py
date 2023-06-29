import requests

for i in range(1,11):
  print(f'Page {i}')
  r = requests.get(f'https://quotes.toscrape.com/page/{i}')
  print(r.status_code)
  html = r.text
  with open('quotes.txt', 'a', encoding='utf-8') as f:
    for line in html.split('\n'):
      if '<span class="text" itemprop="text">“' in line:
        line = line.replace('<span class="text" itemprop="text">“', '').replace('”</span>', '')
        line = line.strip()
        print(line)
        f.write(line)
        f.write('\n')    
