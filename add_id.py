import random

with open("chromedriver/anekdots.txt", "r", encoding="utf_8") as file:
    list_anekdots = file.readlines()

new_list = []

for item in list_anekdots:
    item = item.strip()
    rnd = random.randrange(1111111111, 99999999999)
    new_str = f"{item}id={rnd}\n"

    new_list.append(new_str)

with open("chromedriver/anekdots.txt", "w", encoding="utf_8") as file:
    file.writelines(new_list)
