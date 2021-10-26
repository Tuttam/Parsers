import requests
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random


def get_source_html(url):
    # service = Service("D:\\MySoft\\ForPython\\Parsers\\chromedriver\\chromedriver.exe")
    # driver = Chrome(service=service)
    # driver.maximize_window()
    #
    # try:
    #     driver.get(url=url)
    #     time.sleep(5)
    #     count_posts = 0
    #     while True:
    #
    #         all_posts = driver.find_elements(By.CLASS_NAME, "card-image-one-column-view__clickable")
    #         count_posts_after_scroll = len(all_posts)
    #
    #         if count_posts_after_scroll == count_posts:
    #             src = driver.page_source
    #             with open("temp_html.html", "w", encoding="utf-8") as file:
    #                 file.write(src)
    #             print(len(all_posts))
    #             break
    #
    #         count_posts = count_posts_after_scroll
    #
    #         body = driver.find_element(By.TAG_NAME, "body")
    #         body.send_keys(Keys.END)
    #         time.sleep(3)
    #
    # except Exception as _ex:
    #     print(_ex)
    # finally:
    #     driver.close()
    #     driver.quit()

    # parse_links()

    parse_texts()


# Парсим ссылки:

def parse_links():
    with open("temp_html.html", "r", encoding="utf-8") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")

    all_posts = soup.find_all(class_="card-image-one-column-view__content")

    link_list = []

    for item in all_posts:
        check_for_img = item.find_all(class_="card-layer-image-view__image _is-loaded")
        if len(check_for_img) > 0:
            link = item.find("a")
            link = link.get("href")
            link_list.append(f"{link}\n")
            # print(link.get("href"))
        else:
            with open("temp_links.txt", "w", encoding="utf-8") as file:
                file.writelines(link_list)
            break


def parse_texts():

    with open("temp_links.txt", "r", encoding="utf-8") as file:
        links_list = file.readlines()

    for i in range(0, len(links_list) - 1):

        print(f"Итерация {i + 1}")

        link = links_list.pop(0)
        link = link.rstrip()

        req = requests.get(url=link, headers=headers)
        src = req.text

        src = src.replace("<br/>", "||")

        soup = BeautifulSoup(src, "lxml")

        all_anecdotes = soup.find_all(class_="article-render__block article-render__block_unstyled")

        all_photos = soup.find_all("img", class_="article-image-item__image")

        if len(all_photos) > 0:
            for item in all_photos:
                url = item.get("src")
                req = requests.get(url=url)
                response = req.content

                rnd = random.randrange(111111111, 9999999999)
                with open(f"images/{rnd}.jpg", "wb") as file:
                    file.write(response)

        for item in all_anecdotes:
            str = item.text
            if len(str) < 15:
                continue

            with open("anecdotes.txt", "a", encoding="utf-8") as f:
                f.write(f"{str}\n")

        with open("temp_links.txt", "w", encoding="utf-8") as file:
            file.writelines(links_list)

        break


def main():
    get_source_html(url="https://zen.yandex.ru/id/60a679c90b77622f9b40ee87")


if __name__ == "__main__":
    main()
