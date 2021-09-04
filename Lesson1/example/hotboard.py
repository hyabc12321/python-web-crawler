import requests
from bs4 import BeautifulSoup


url = "https://www.ptt.cc/bbs/hotboards.html"
def main():
    r = requests.get(url)
    web_content = r.text
    # print(web_content) 
    soup = BeautifulSoup(web_content, 'html.parser')
    board_name_elements = soup.find_all('div', class_="board-name")
    board_names = [e.text for e in board_name_elements]
    popluarity_elements = soup.find_all('div', class_="board-nuser")
    popularities = [int(e.text) for e in popluarity_elements]
    for pop, bn in zip(popularities, board_names):
        print(pop, bn)
        

if __name__ == '__main__':
    main()