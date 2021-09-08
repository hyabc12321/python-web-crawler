import requests
from bs4 import BeautifulSoup


url = "https://www.ptt.cc/bbs/hotboards.html"
output_filename = 'Lesson1/example/hotboard.txt'

def main():
    r = requests.get(url)
    web_content = r.text
    # print(web_content)
    soup = BeautifulSoup(web_content, 'html.parser')
    board_name_elements = soup.find_all('div', class_="board-name")
    board_names = [e.getText() for e in board_name_elements]
    popluarity_elements = soup.find_all('div', class_="board-nuser")
    popularities = [int(e.getText()) for e in popluarity_elements]
    with open(output_filename, 'w') as f:
        for pop, bn in zip(popularities, board_names):
            f.write(f'{pop}, {bn} \n')


if __name__ == '__main__':
    main()
