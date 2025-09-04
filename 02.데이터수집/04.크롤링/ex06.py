#[네이버]-[네이버항공] 이번달 25~26일 제주도 항공권 검색
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
browser = webdriver.Chrome(options=options)

url = 'https://flight.naver.com/'
browser.get(url)
time.sleep(2)

#7일간 보지않기 버튼
btn = browser.find_element(By.CLASS_NAME, 'FullscreenPopup_suspend')
btn.click()
#time.sleep(5)

#가는날 선택
el = browser.find_element(By.XPATH, '//button[text()="가는 날"]')
el.click()
