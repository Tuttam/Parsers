import requests
from bs4 import BeautifulSoup
import time
from time import sleep

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "ru,ru-RU;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "max-age=0",
    "sec-ch-ua": '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
}


url = "https://www.anekdot.ru/last/anekdot/"
req = requests.get(url=url, headers=headers)

with open("anekdots.txt", "w", encoding="utf-8") as file:
    file.write("")

for i in range(0, 50):
    src = req.text
    src = src.replace("<br>", "|")

    soup = BeautifulSoup(src, "lxml")

    all_anecdots = soup.find_all(class_="text")
    for item in all_anecdots:
        with open("anekdots.txt", "a", encoding="utf-8") as file:
            file.write(f"{item.text}\n")

    next_link = soup.find(class_="voteresult").find("a").get("href")

    url = f"https://www.anekdot.ru{next_link}"

    req = requests.get(url=url, headers=headers)

    print(f"Итерация {i + 1}")

    sleep(2)
