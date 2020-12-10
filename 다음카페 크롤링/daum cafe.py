import time
import pandas as pd

from bs4 import BeautifulSoup
from selenium import webdriver as wd
import re

cafe_title = []
url = "https://m.cafe.daum.net/-ohmygirl/_rec?boardType=M"
# instagram_tags = []
driver = wd.Chrome("/Users/kimsiwoo/Desktop/WORKSPACE/PYTHON/크롤링/chromedriver")
# 크롬드라이버 지정
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

driver.get(url)     # 지정한 페이지 크롬드라이버로 띄우기

time.sleep(3)
driver.find_element_by_xpath('//*[@id="cafe_navi_default"]/span/a').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="mArticle"]/div/div/div/div[3]/a[1]/span[2]').click()
time.sleep(3)
elem_login = driver.find_element_by_name("email")
elem_login.clear()
elem_login.send_keys('kimsiwookim@daum.net')
elem_login = driver.find_element_by_name('password')
elem_login.clear()
elem_login.send_keys('kim54951!!')
time.sleep(2)
driver.find_element_by_xpath('//*[@id="login-form"]/fieldset/div[8]/button[1]').click()
time.sleep(3)
# 자동로그인
for page in range(487900,488217) :
    try :
        pages = "http://cafe.daum.net/-ohmygirl/XthE/" + str(page)
        driver.get(pages)
        driver.switch_to_frame("down")      # iframe으로 html이 숨겨져 있었기 때문에 이걸로 주소를 따옴
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'lxml')
        title_raw = soup.find('strong', class_='tit_info')
        title = re.findall('[A-Za-z0-9가-힣]+', str(title_raw))   # str로 뽑아 리스트 만듬
        # 불필요한 요소 제
        del title[:4]
        title.remove("strong")
        for title_one in title:
            cafe_title.append(title_one)  # 인스타태그 리스트에 단어들 추가
    except :
        pass
    # tags = re.findall('[A-Za-z0-9가-힣]+', title_raw)
    # tag = ''.join(tags).replace("#"," ") # "#" 제거
    # tag_data = tag_raw.split()      # 모은것들 단어 별로 분리하
driver.close()

results = pd.DataFrame(cafe_title)      # 인스타태그 리스트 데이터 프레임으로 변환
results.to_csv('daum cafe results.csv', encoding='UTF-8')     # 파일 저장