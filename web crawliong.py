#import time

#from selenium.webdriver.common.keys import Keys
#from bs4 import BeautifulSoup as bs
#from selenium import webdriver

#driver = webdriver.Chrome(r'/Users/saehyunlim/Downloads/chromedriver')  # chrome driver가 깔려있는 경로를 절대경로로 지정해준다.
#driver.get('http://www.google.com') # 구글로 이동
#target=driver.find_element_by_css_selector("[name = 'q']")
#target.send_keys('밀알학교') # 검색창에 타겟입력
#target.send_keys(Keys.ENTER) # 엔터
#news = driver.find_element_by_css_selector('#hdtb-msb > div:nth-child(1) > div > div:nth-child(2) > a') #뉴스탭
#news.click() #뉴스탭클릭
#driver.get('https://www.google.com') #
#target=driver.find_element_by_css_selector("[name = 'q']")
#target.send_keys('밀알학교에서 임세현 얼굴 찾기') # 검색창에 타겟입력
#time.sleep(3)
#driver.quit()
#target.send_keys(Keys.Enter)
#target.send_keys(Keys.Enter)
#newsd = driver.find_element_by_css_selector('#hdtb-msb > div:nth-child(1) > div > div:nth-child(2) > a') #뉴스탭
#newsd.click() #뉴스탭클릭
#driver.get('https://www.google.com/search?q=%EB%B0%80%EC%95%8C%ED%95%99%EA%B5%90&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiGgq_izpz0AhWHsVYBHZjhAQoQ_AUoAXoECAEQAw&biw=1244&bih=638&dpr=2#imgrc=dbauuxdFMJP92M')
#driver.quit