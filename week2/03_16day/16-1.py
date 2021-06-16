import requests
from bs4 import BeautifulSoup
# 네이버 영화 목록 스크래핑(제목, 평점)
# beautifulsoup4 -> HTML 파싱을 편리하게
# requests -> 브라우저에서 엔터를 치는 효과. URL에 요청하기
# URL을 읽어서 HTML를 받아오고, 헤더를 넣어주는건 정보를 긁어오는게 사람이라고 인증시켜주는 것
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, tr들을 불러오기
movies = soup.select('#old_content > table > tbody > tr')

#여기부터는 본인의 입맛대로 코딩!!
#############################

# movies (tr들) 의 반복문을 돌리기
rank = 1
for movie in movies:
    a_tag = movie.select_one('td.title > div > a')
    if a_tag is not None:   # a_tag가 None값이 아니면 타이틀과 평점을 프린트 해준다
        title = a_tag.text  # 제목
        star = movie.select_one('td.point').text #평점
        print(rank,title,star) #프린트!!
        rank += 1 #랭킹

#############################