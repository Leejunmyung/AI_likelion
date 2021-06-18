from bs4 import BeautifulSoup
from urllib.request import urlopen
m_url = 'https://movie.naver.com/movie/running/premovie.nhn'
page = urlopen(m_url)
soup = BeautifulSoup(page,'html.parser')
title = soup.select_one(' dt > a').text
star = soup.select_one('span.num').text
people = soup.select_one('span.num2 > em').text
summary = soup.select_one('dd:nth-child(2) > span.link_txt > a').text
derector = soup.select_one('dd:nth-child(4) > span.link_txt > a').text
print(title, star, people,summary,derector)
#content > div.article > div:nth-child(1) > div:nth-child(5) > ul > li > dl > dd:nth-child(3) > dl > dd:nth-child(4) > span > a
