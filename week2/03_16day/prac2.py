from bs4 import BeautifulSoup
from urllib.request import urlopen
m_url = 'https://movie.naver.com/movie/running/current.nhn#'
page = urlopen(m_url)
soup = BeautifulSoup(page, "html.parser")
movies = soup.select('#content > div.article > div:nth-child(1) > div.lst_wrap > ul > li')
print('영화제목\t ','평점\t','참여\t','애매율\t\t','감독\n')

for movie in movies:
    title = movie.select_one(' dl > dt > a').text
    star = movie.select_one('span.num').text
    people = movie.select_one('em').text
    rate = movie.select_one(' div > span.num')
    king = movie.select_one('dd:nth-child(4) > span > a').text
    if rate is not None:
        a = rate.text
        print(title + '\t', star + '\t', people + '\t', a + '\t', king + '\n')
    else:
        a = '0'
        print(title + '\t', star + '\t', people + '\t', a + '\t', king + '\n')