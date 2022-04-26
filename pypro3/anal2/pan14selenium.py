'''Created on 2022. 4. 20. 7교시~ '''
# 셀레니움으로 브라우저를 띄워 제어를 할 수 있다.

from selenium import webdriver

try:
    url = "https://www.daum.net"
    browser = webdriver.Chrome('C:/work/chromedriver')
    browser.implicitly_wait(3)
    browser.get(url);
    browser.save_screenshot("daum_img.png")
    
    browser.quit()

    print('성공')
except Exception:
    print('에러')