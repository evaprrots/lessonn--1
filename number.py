try:
    number_str = input("Введіть число: ")
    number = int(number_str)
    print("Ви ввели число:", number)
except ValueError:
    print("Помилка: введені дані не можна конвертувати в ціле число!")
