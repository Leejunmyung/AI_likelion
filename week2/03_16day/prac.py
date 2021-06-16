import requests
from bs4 import BeautifulSoup
data = requests.get('https://finance.naver.com/sise/')
soup = BeautifulSoup(data.text, 'html.parser')
likes = soup.select('#contentarea > div.box_top_submain2 > div.rgt> #popularItemList > li')
rank = 1
for like in likes:
    a = like.select_one('a')
    if a is not None:
        title = a.text
        updown = like.select_one('span').text
        print(rank,title,updown)
        rank += 1