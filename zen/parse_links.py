from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


def get_source_html(url):

    try:
        service = Service("C:\\bin\\chromedriver.exe")
        driver = Chrome(service=service)
        driver.maximize_window()

        driver.get(url=url)
        time.sleep(5)
        count_posts = 0
        while True:

            all_posts = driver.find_elements(By.CLASS_NAME, "card-image-one-column-view__clickable")
            count_posts_after_scroll = len(all_posts)

            if count_posts_after_scroll == count_posts:
                src = driver.page_source
                with open("temp_html.html", "w", encoding="utf-8") as file:
                    file.write(src)
                print(len(all_posts))
                break

            count_posts = count_posts_after_scroll

            body = driver.find_element(By.TAG_NAME, "body")
            body.send_keys(Keys.END)
            time.sleep(3)

    except Exception as _ex:
        print(_ex)
    finally:
        driver.close()
        driver.quit()

    parse_links()


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

    with open("src/temp_links.txt", "w", encoding="utf-8") as file:
        file.writelines(link_list)


def main():
    get_source_html(url="https://zen.yandex.ru/id/60aab81c5ac79559a3193eb6")


if __name__ == "__main__":
    main()
