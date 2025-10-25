a = float(input("Введи перше число (a): "))
b = float(input("Введи друге число (b): "))
operation = input("Вкажи дію (+, -, *, /): ")

if operation == "+":
    print(f"Результат: {a + b}")
elif operation == "-":
    print(f"Результат: {a - b}")
elif operation == "*":
    print(f"Результат: {a * b}")
elif operation == "/":
    if b == 0:
        print("Помилка: ділення на нуль!")
    else:
        print(f"Результат: {a / b}")
else:
    print("Невідома операція!")
