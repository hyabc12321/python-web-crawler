import requests
from bs4 import BeautifulSoup


url = "https://www.ptt.cc/bbs/hotboards.html"

def main():
    response = requests.get(url)
    web_content = response.text
    # print(web_content)
    content = BeautifulSoup(web_content, 'html.parser')
    board_name_elements = content.find_all('div', class_="board-name")
    
    board_names = []
    for element in board_name_elements:
        board_names.append(element.getText())

    popluarity_elements = content.find_all('div', class_="board-nuser")
    popularities = [int(e.getText()) for e in popluarity_elements]

    output_filename = 'Lesson1/example/hotboard.txt'
    with open(output_filename, 'w') as file:
        for i in range(len(board_names)):
            file.write(f'{board_names[i]}: {popularities[i]} \n')


if __name__ == '__main__':
    main()
