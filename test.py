import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver as wd
import re

bunjang_title = []
bunjang_address = []

url = "https://m.bunjang.co.kr/search/products?q=%EC%98%A4%EB%A7%88%EC%9D%B4%EA%B1%B8&order=popular&page=1"
# instagram_tags = []
driver = wd.Chrome("/Users/kimsiwoo/Desktop/WORKSPACE/PYTHON/chromedriver")
# 크롬드라이버 지정

driver.get(url)     # 지정한 페이지 크롬드라이버로 띄우기

for page in range(1,2) :
        pages = "https://m.bunjang.co.kr/search/products?q=%EC%98%A4%EB%A7%88%EC%9D%B4%EA%B1%B8%20%ED%8F%AC%ED%86%A0%EC%B9%B4%EB%93%9C&order=date&page=" + str(page)
        driver.get(pages)
        time.sleep(2)
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')
        # 가격 추출
        title_raw = soup.select('div.sc-ivVeuv.dRQJkv')
        title = re.findall('[0-9]+,[0-9]+', str(title_raw))  # str로 뽑아 리스트 만듬
        for title_one in title:
            bunjang_title.append(title_one)
        print(bunjang_title)
driver.close()


# results = pd.DataFrame(bunjang_title)      # 인스타태그 리스트 데이터 프레임으로 변환
# results.to_csv('bunjang results.csv', encoding='UTF-8')     # 파일 저장