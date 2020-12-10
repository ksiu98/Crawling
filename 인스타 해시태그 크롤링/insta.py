import requests
from selenium import webdriver as wd
import time
import re
import pandas as pd

keyword = "오마이걸"        # 검색할 키워드 할당
url = "https://www.instagram.com/explore/tags/{}/".format(keyword)
# 인스타그램 키워드 검색한 페이지 지정

instagram_tags = []
driver = wd.Chrome("/Users/kimsiwoo/Desktop/WORKSPACE/PYTHON/chromedriver")
# 크롬드라이버 지정
driver.get(url)     # 지정한 페이지 크롬드라이버로 띄우기
time.sleep(3)

login_section = '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/span/a[1]/button'
driver.find_element_by_xpath(login_section).click()
time.sleep(3)
elem_login = driver.find_element_by_name("username")
elem_login.clear()
elem_login.send_keys('siu_9898')
elem_login = driver.find_element_by_name('password')
elem_login.clear()
elem_login.send_keys('kim54951!!')
time.sleep(2)
elem_login.submit()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/section/div/button').click()
# 자동 로그인
driver.get(url)     # 지정한 페이지 크롬드라이버로 띄우기
time.sleep(7)

driver.find_element_by_css_selector('.v1Nh3.kIKUG._bz0w').click()       # 첫번째 게시글 클릭
for i in range(150):
    time.sleep(3)
    data = driver.find_element_by_css_selector('.C7I1f.X7jCj') # C7I1f X7jCj    # 인스타 게시물 태그 좌표
    tag_raw = data.text
    tags = re.findall('#[A-Za-z0-9가-힣]+', tag_raw)  # 태그 수집
    tag = ''.join(tags).replace("#"," ") # "#" 제거
    tag_data = tag.split()      # 모은것들 단어 별로 분리하
    next = driver.find_element_by_css_selector('a._65Bje.coreSpriteRightPaginationArrow')  # 우측화살표
    next.click()   # 우측화살표 클릭으로 다음 게시물 이동

    for tag_one in tag_data:
        instagram_tags.append(tag_one)  # 인스타태그 리스트에 단어들 추가
driver.close()

results = pd.DataFrame(instagram_tags)      # 인스타태그 리스트 데이터 프레임으로 변환
results.to_csv('results.csv', encoding='UTF-8')     # 파일 저장