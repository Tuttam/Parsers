import random

with open("chromedriver/anekdots.txt", "r", encoding="utf_8") as file:
    list_anecdotes = file.readlines()

with open("data/used_id.txt", "r", encoding="utf_8") as file:
    list_id = file.readlines()

with open("chars.txt", "r", encoding="utf_8") as file:
    list_char = file.readlines()

one_char = list_char.pop(0)
one_char = one_char.strip()
list_char.append(f"{one_char}\n")

with open("chars.txt", "w", encoding="utf_8") as file:
    file.writelines(list_char)

print(list_char)

rand_int_char = random.randrange(4, 7)
str_char = one_char

for i in range(0, rand_int_char):
    str_char += one_char

print(str_char)

for i in range(0, 20):

    end_num = len(list_anecdotes) - 1
    rnd = random.randrange(0, end_num)

    fetch_str = list_anecdotes[rnd]
    fetch_str = fetch_str.strip()

    anecdote = fetch_str.split("id=")[0]
    anecdote_split = anecdote.split("|")
    anecdote = anecdote.replace("|", "\n")

    list_anecdotes.pop(rnd)

    with open("chromedriver/used_anekdots.txt", "a", encoding="utf_8") as file:
        file.write(f"{fetch_str}\n")

    with open("data/import.txt", "a", encoding="utf_8") as file:
        file.write(f"{anecdote}\r{str_char}\r")

    with open("chromedriver/anekdots.txt", "w", encoding="utf_8") as file:
        file.writelines(list_anecdotes)

with open("data/import.txt", "a", encoding="utf_8") as file:
        file.write(f"\r===============\r \r")


    # print(len(list_anecdotes))
    # print(anecdote)
