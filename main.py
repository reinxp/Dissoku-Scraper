import  requests 
from bs4 import BeautifulSoup
import threading
import time


Word = input("検索したいワードを入力してください:")
page = input("検索したいページを入力してください:")
print("検索中です....")
response = requests.get(f'https://dissoku.net/ja/search/result?q={Word}&page={page}')
soup = BeautifulSoup(response.text, 'lxml')
invite = soup.find_all('a', id='bottom-btn__inner',class_="join-btn bottom-btn__inner v-btn v-btn--has-bg theme--dark v-size--default")
guild_name = soup.find_all('a',style="color:aliceblue;text-decoration:none;")

def search1():
 for link in invite:
    with open('output.txt',mode='a', encoding='utf-8') as f:
       invites = link.get('href')
       time.sleep(1.5)
       links = requests.get(invites).url
       print(links)
       f.write(links+"\n")

def search2():
 for name in guild_name:
    with open('output.txt',mode='a', encoding='utf-8') as f:
       names = name.get("title")
       time.sleep(2)
       print(names)
       f.write(names+"\n")

def main():
    t1 = threading.Thread(target=search1)
    t2 = threading.Thread(target=search2)
    t1.start()
    t2.start()
if __name__ == "__main__":
    main()