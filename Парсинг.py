from bs4 import BeautifulSoup
import urllib.request

req = urllib.request.urlopen('https://www.championat.com/football/')
html = req.read()

soup = BeautifulSoup(html, "html.parser")

# print(soup)

news = soup.find_all('li', class_='news-item')

# print(news)

results = []

for item in news:
    title = item.findNext('a', target='_top').get_text()
    # print(title)
    desc = None
    # print(desc)
    href = item.a.get('href')
    # print(href)
    results.append({
        'title': title,
        'desc': None,
        'href': href,
    })

f = open('news.txt', 'w', encoding='utf-8')
i = 1
for item in results:
    f.write(f'Новость N{i}\n\nНазвание: {item["title"]}\nСсылка: {item["href"]}\n\n*********\n')
    i += 1
f.close()