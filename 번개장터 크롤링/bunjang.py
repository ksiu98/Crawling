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

for page in range(1,10) :
        try :
                pages = "https://m.bunjang.co.kr/search/products?q=%EC%98%A4%EB%A7%88%EC%9D%B4%EA%B1%B8&order=popular&page=" + str(page)
                driver.get(pages)
                time.sleep(2)
                page_source = driver.page_source
                soup = BeautifulSoup(page_source, 'html.parser')

        # 제목 추출
                title_raw = soup.select('div.sc-dTLGrV.iuakOf')
                title = re.findall('[A-Za-z0-9가-힣]+', str(title_raw))  # str로 뽑아 리스트 만듬
                title = set(title)  # 집합set으로 변환
                title.remove("div")
                title.remove("class")
                title.remove("sc")
                title.remove("dTLGrV")
                title.remove("iuakOf")
                title = list(title)  # list로 변환
                for title_one in title:
                 bunjang_title.append(title_one)

        # 주소 추출
                address_raw = soup.select('div.sc-cCbXAZ.dyRrjH')
                address = re.findall('[가-힣]+', str(address_raw))  # str로 뽑아 리스트 만듬
                address = set(address)  # 집합set으로 변환
                address = list(address)  # list로 변환
                for address_one in address:
                    bunjang_address.append(address_one)
        except :
                pass
driver.close()


results = pd.DataFrame(bunjang_title)
results.to_csv('bunjang title.csv', encoding='UTF-8')     # 파일 저장
results = pd.DataFrame(bunjang_address)
results.to_csv('bunjang address.csv', encoding='UTF-8')     # 파일 저장