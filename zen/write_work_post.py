import random
import os
import shutil
from PIL import Image


login = "vasilisatcheshkova"


def main():

    check_create_files()

    create_content()

    create_images()


def check_create_files():

    if os.path.exists(f"work-files/{login}"):
        pass
    else:
        os.mkdir(f"work-files/{login}")

    if os.path.exists(f"work-files/{login}/img"):
        pass
    else:
        os.mkdir(f"work-files/{login}/img")

    if os.path.isfile(f"work-files/{login}/{login}_images.txt"):
        pass
    else:
        with open(f"work-files/{login}/{login}_images.txt", "w", encoding="utf-8") as f:
            f.write("")

    if os.path.isfile(f"work-files/{login}/{login}_id.txt"):
        pass
    else:
        with open(f"work-files/{login}/{login}_id.txt", "w", encoding="utf-8") as f:
            f.write("")


def create_content():

    with open(f"work-files/{login}/{login}_content.txt", "w", encoding="utf-8") as f:
        f.write("")

    with open(f"src/anecdotes.txt", "r", encoding="utf-8") as f:
        list_anecdotes = f.readlines()

    with open(f"work-files/{login}/{login}_id.txt", "r", encoding="utf-8") as f:
        list_id = f.readlines()

    # Смайлы:

    with open("chars.txt", "r", encoding="utf_8") as file:
        list_char = file.readlines()

    one_char = list_char.pop(0)
    one_char = one_char.strip()
    list_char.append(f"{one_char}\n")

    with open("chars.txt", "w", encoding="utf_8") as file:
        file.writelines(list_char)

    rand_int_char = random.randrange(4, 7)
    str_char = one_char

    for i in range(0, rand_int_char):
        str_char += one_char

    rnd_num_of_posts = random.randrange(14, 17)

    for i in range(0, rnd_num_of_posts):

        rnd_string = random.randrange(0, len(list_anecdotes) - 1)

        one_anecdote_data = list_anecdotes[rnd_string]
        one_anecdote = one_anecdote_data.split("id=")[0]

        anecdote_id = one_anecdote_data.split("id=")[1].strip()
        anecdote_id = int(anecdote_id)

        test_out = 0

        for item in list_id:
            test_id = item.strip()
            test_id = int(test_id)

            if anecdote_id == test_id:
                i -= 1
                test_out = 1
                break

        if test_out != 0:
            test_out = 0
            continue

        with open(f"work-files/{login}/{login}_id.txt", "a", encoding="utf-8") as f:
            f.write(f"{anecdote_id}\n")

        one_anecdote = one_anecdote.replace("||", "\n")

        with open(f"work-files/{login}/{login}_content.txt", "a", encoding="utf-8") as f:
            f.write(f"{one_anecdote}\n{str_char}\n")


def create_images():

    list_del_img = os.listdir(f"work-files/{login}/img")
    for item in list_del_img:
        os.remove(f"work-files/{login}/img/{item}")

    for_while = 0

    while for_while < 2:

        with open(f"work-files/{login}/{login}_images.txt", "r", encoding="utf-8") as f:
            list_black_images = f.readlines()

        list_work_images = os.listdir("images")

        rnd_num_image = random.randrange(0, len(list_work_images) - 1)

        image_for_work = f"images/{list_work_images[rnd_num_image]}"
        print(image_for_work)
        for_test = 0

        for item in list_black_images:
            if item.strip() == image_for_work.strip():
                for_test = 1
                break

        if for_test != 0:
            continue

        with open(f"work-files/{login}/{login}_images.txt", "a", encoding="utf-8") as f:
            f.write(f"{os.path.basename(image_for_work)}\n")



        img = shutil.copy(image_for_work, f"worked_images")

        work_image = Image.open(img)
        os.remove(image_for_work)

        rnd_pixels = random.randrange(30, 50)
        new_width = work_image.size[0] - rnd_pixels

        rnd_pixels = random.randrange(30, 50)
        new_height = work_image.size[1] - rnd_pixels

        new_img = work_image.resize((new_width, new_height))

        rnd_file_name = random.randrange(111111111, 99999999999)
        new_img.save(f"work-files/{login}/img/{rnd_file_name}.png")

        path_finished_img = os.path.abspath(f"work-files/{login}/img/{rnd_file_name}.png")

        with open(f"work-files/{login}/{login}_content.txt", "a", encoding="utf-8") as f:
            f.write(f"{path_finished_img}\n")

        print(os.path.abspath(path_finished_img))

        for_while += 1


if __name__ == "__main__":
    main()
