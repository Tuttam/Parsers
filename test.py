import random

# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# random.shuffle(numbers)
# # print(numbers)
# # random_number = random.choice(numbers)
# print(numbers[(len(numbers) - 1)])

a = [5,9,6,2,3]
b = [1,4,5,6,17]
t = 0
for i in a:
    for j in b:
        if i == j:
            print(f"{i} == {j}")
            t = 1
            break
        else:
            print(f"{i} != {j}")

    print(f"_____________")
    if t != 0:
        t = 0
        continue

    print(f"+++++++++++++")
