import requests
from bs4 import BeautifulSoup


url = 'https://news.ltn.com.tw/list/breakingnews/popular'
article_dir = 'Lesson1/example/hot_articles'
def main():
    r = requests.get(url)
    web_content = r.text
    content = BeautifulSoup(web_content, 'html.parser')
    news_list = content.find_all('a', class_='tit')
    titles = []
    hrefs = []
    for news in news_list:
        # print(f"{news.get('title')} {news.get('href')}")
        titles.append(news.get('title'))
        hrefs.append(news.get('href'))

    for i in range(len(titles)):
        r = requests.get(hrefs[i])
        web_content = r.text
        content = BeautifulSoup(web_content, 'html.parser')
        article_title = content.find('h1').getText()
        article_content = content.find('div', class_='text')
        article_content.find('p', class_='appE1121').decompose()
        article_content = article_content.getText()

        output_filename = f'{article_dir}/{titles[i]}.txt'
        with open(output_filename, 'w') as f:
            f.write(f'Title: {article_title} \n')
            f.write(f'Content: {article_content} \n')


if __name__ == '__main__':
    main()