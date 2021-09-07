import requests
from bs4 import BeautifulSoup


url = 'https://womany.net/read/article/27639?ref=h-hot-0'
output_filename = 'Lesson1/example/article.txt'


def main():
    r = requests.get(url)
    web_content = r.text
    soup = BeautifulSoup(web_content, 'html.parser')
    article_title = soup.find(itemprop="name headline").getText()
    article_content = soup.find(class_="article-body").getText()
    with open(output_filename, 'a') as f:
        f.write(f'Title: {article_title}')
        f.write(f'Content: {article_content}')


if __name__ == '__main__':
    main()
