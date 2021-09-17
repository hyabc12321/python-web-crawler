import requests
from bs4 import BeautifulSoup


url = 'https://womany.net/read/article/27639?ref=h-hot-0'
output_filename = 'Lesson1/example/article.txt'


def main():
    r = requests.get(url)
    web_content = r.text
    content = BeautifulSoup(web_content, 'html.parser')
    article_title = content.find(itemprop="name headline").getText()
    article_content = content.find(class_="article-body").find('h2')
    for line in article_content:
        print(line.getText())
    # with open(output_filename, 'w') as f:
    #     f.write(f'Title: {article_title}')
    #     f.write(f'Content: {article_content}')


if __name__ == '__main__':
    main()
