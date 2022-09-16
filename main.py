from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import time
import schedule
from message_sender import send_msg

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://m.ticket.yes24.com/Perf/36086")
# driver.get("http://m.ticket.yes24.com/Perf/Detail/PerfInfo.aspx?IdPerf=43506")

cnt = 0


def get_site_info():
    driver.refresh()
    global cnt
    cnt += 1
    available = False
    book_btn = False
    closed_btn = driver.find_element(By.CLASS_NAME, "btn_dGray")

    try:
        book_btn = driver.find_element(By.CLASS_NAME, "btn_red")
    except:
        pass

    if closed_btn:
        available = False

    if book_btn:
        available = True

    if available:
        send_msg('지금! 예매 가능합니다!')
    else:
        print('예매 불가합니다 ' + str(cnt) + '초 동안 진행중')


def send_check_msg():
    send_msg(f'걱정마세요! {cnt}동안 잘 실행되고 있습니다!')


schedule.every(1).seconds.do(get_site_info)
schedule.every(1).hours.do(send_check_msg)

while True:
    schedule.run_pending()
    time.sleep(1)
