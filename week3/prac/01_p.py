reviews = soup.select('#cm_cr-review_list > div')
for review in reviews:
    try:
        iname=review.select_one('div.a-profile-content > span').text
        istar=review.select_one('div:nth-child(2) > a:nth-child(1) > i > span').text
        idate=review.select_one('span.a-size-base').text
        iview=review.select_one('span.a-size-base > span').text
        icount=review.select_one('span.cr-vote > div.a-row.a-spacing-small > span').text
        print(icount)
    except Exception as e:
        continue