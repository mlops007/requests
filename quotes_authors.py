import requests

for i in range(1,11):

  r = requests.get(f'https://quotes.toscrape.com/page/{i}')
  print(i,r.status_code)
  html = r.text

  with open('combined.csv', 'a', encoding='utf-8') as f:

    for line in html.split('\n'):

          if '<span class="text" itemprop="text">“' in line:
            quote = line.replace('<span class="text" itemprop="text">“', '').replace('”</span>', '')
            quote = quote.strip()
            

          if '<span>by <small class="author" itemprop="author">' in line:
            author = line.replace('<span>by <small class="author" itemprop="author">', '').replace('</small>', '')
            author = author.strip()

            print(quote)
            print(author)

            f.write(author + ',' + quote)
            f.write('\n') 

