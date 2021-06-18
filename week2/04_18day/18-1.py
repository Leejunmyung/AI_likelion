from bs4 import BeautifulSoup
from urllib.request import urlopen
m_url = 'https://movie.naver.com/movie/running/premovie.nhn'
page = urlopen(m_url)
soup = BeautifulSoup(page,'html.parser')
movie = soup.select_one('#content > div.article > div:nth-child(1) > div:nth-child(5) > ul > li > dl > dt > a')
print(movie.text)
