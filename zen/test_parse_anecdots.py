import requests
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import random


with open("temp_links.txt", "r", encoding="utf-8") as file:
    links_list = file.readlines()

service = Service("D:\\ForPython\\Parsers\\chromedriver\\chromedriver.exe")
driver = Chrome(service=service)
driver.maximize_window()

try:
    for i in range(0, len(links_list)):
        print(f"Итерация {i + 1}")

        link = links_list.pop(0)
        url = link.rstrip()

        driver.get(url=url)
        WebDriverWait(driver, timeout=10)
        sleep(1)

        src = driver.page_source

        src = src.replace("<br>", "||")
        soup = BeautifulSoup(src, "lxml")

        all_anecdotes = soup.find_all(class_="article-render__block article-render__block_unstyled")

        for item in all_anecdotes:
            str = item.text
            if len(str) < 15:
                continue

            with open("anecdotes.txt", "a", encoding="utf-8") as f:
                f.write(f"{str}\n")

        all_images = soup.find_all(class_="article-image-item__image")

        if len(all_images) > 0:

            for item in all_images:
                link_img = item.get("src")

                req = requests.get(url=link_img)
                response = req.content

                rnd = random.randrange(111111111, 9999999999)
                with open(f"images/{rnd}.jpg", "wb") as file:
                    file.write(response)

                sleep(1)

        with open("temp_links.txt", "w", encoding="utf-8") as file:
            file.writelines(links_list)

except Exception as _ex:
    print(_ex)
finally:
    driver.close()
    driver.quit()
