points = int(input("Введи кількість балів: "))

if 0 <= points <= 49:
    print("Незадовільно")
elif 50 <= points <= 69:
    print("Задовільно")
elif 70 <= points <= 89:
    print("Добре")
elif 90 <= points <= 100:
    print("Відмінно")
else:
    print("Некоректна кількість балів!")
