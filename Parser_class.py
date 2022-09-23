from bs4 import BeautifulSoup
import urllib.request


class Parser:
    raw_html = ""
    html = ""
    results = []

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        req = urllib.request.urlopen(self.url)
        self.raw_html = req.read()
        self.html = BeautifulSoup(self.raw_html, "html.parser")

    def parsing(self):
        news = self.html.find_all('li', class_='news-item')

        for item in news:
            title = item.findNext('a', target='_top').get_text()
            desc = None
            href = item.a.get('href')
            # print(href)
            self.results.append({
                'title': title,
                'desc': None,
                'href': href,
            })

    def save(self):
        with open(self.path, 'w', encoding='utf-8') as f:
            i = 1
            for item in self.results:
                f.write(f'Новость N{i}\n\nНазвание: {item["title"]}\nСсылка: {item["href"]}\n\n{" * " * 10}\n')
                i += 1

    def run(self):
        self.get_html()
        self.parsing()
        self.save()
