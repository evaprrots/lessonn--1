import random

number = random.randint(1, 10)
attempts = 3

print("Гра 'Вгадай число від 1 до 10'!")

for i in range(attempts):
    guess = int(input("Введи число: "))

    if guess == number:
        print("Вітаю! Ти вгадав число!")
        break
    elif guess > number:
        print("Менше!")
    else:
        print("Більше!")

    if i == attempts - 1:
        print(f"На жаль, спроби закінчилися. Загадане число було {number}.")
