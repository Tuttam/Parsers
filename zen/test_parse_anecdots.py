import requests
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random


with open("temp_links.txt", "r", encoding="utf-8") as file:
    links_list = file.readlines()

for i in range(0, len(links_list) - 1):

    print(f"Итерация {i + 1}")

    link = links_list.pop(0)
    url = link.rstrip()

    service = Service("D:\\ForPython\\Parsers\\chromedriver\\chromedriver.exe")
    driver = Chrome(service=service)
    driver.maximize_window()

    try:
        driver.get(url=url)
        WebDriverWait(driver, timeout=10)

        el = driver.find_element(By.CLASS_NAME, "article-image-item__image")
        el.screenshot("111.png")
        # time.sleep(5)
        # driver.find_elements(By.CLASS_NAME, "")
    except Exception as _ex:
        print(_ex)
    finally:
        driver.close()
        driver.quit()




    # src = src.replace("<br/>", "||")
    #
    # soup = BeautifulSoup(src, "lxml")
    #
    # all_anecdotes = soup.find_all(class_="article-render__block article-render__block_unstyled")
    #
    # all_photos = soup.find_all("img", class_="article-image-item__image")
    #
    # print(all_photos)
    # break
    #
    # if len(all_photos) > 0:
    #     for item in all_photos:
    #         url = item.get("src")
    #         req = requests.get(url=url)
    #         response = req.content
    #
    #         rnd = random.randrange(111111111, 9999999999)
    #         with open(f"images/{rnd}.jpg", "wb") as file:
    #             file.write(response)
    #
    # for item in all_anecdotes:
    #     str = item.text
    #     if len(str) < 15:
    #         continue
    #
    #     with open("anecdotes.txt", "a", encoding="utf-8") as f:
    #         f.write(f"{str}\n")
    #
    # with open("temp_links.txt", "w", encoding="utf-8") as file:
    #     file.writelines(links_list)

    break



