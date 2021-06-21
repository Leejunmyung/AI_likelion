from selenium import webdriver
from bs4 import BeautifulSoup
driver = webdriver.Chrome('chromedriver')
url = 'https://www.amazon.com/Samsung-Chromebook-Plus-Camera-Chrome/product-reviews/B07J1SY5QQ/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber='
driver.get(url)
all_user = []
all_star = []
all_date = []
all_review = []
page = driver.page_source
soup = BeautifulSoup(page,'html.parser')
reviews = soup.select('#cm_cr-review_list > div')
for review in reviews:
    try:
        iname=review.select_one('div.a-profile-content > span').text
        istar=review.select_one('div:nth-child(2) > a:nth-child(1) > i > span').text
        idate=review.select_one('span.a-size-base').text
        iview=review.select_one('span.a-size-base > span').text
        all_user.append(iname)
        all_star.append(istar)
        all_date.append(idate)
        all_review.append(iview)
        print(iname,istar)
    except Exception as e:
        continue