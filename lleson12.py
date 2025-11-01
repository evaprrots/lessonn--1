class DatabaseManager:
    def __init__(self):
        self.data = []

    def save_data(self, item):
        """Зберігає дані (поки що у список)"""
        self.data.append(item)
        print(f"[DB] Дані збережено: {item}")

    def get_all_data(self):
        """Повертає всі дані"""
        return self.data


class WebParser:
    def __init__(self, source_url):
        self.source_url = source_url

    def parse(self):
        """Парсить сайт (тут просто імітація отримання даних)"""
        print(f"[Parser] Парсинг сайту: {self.source_url}")
        fake_data = ["Новина 1", "Новина 2", "Новина 3"]
        return fake_data


class UserInterface:
    def show_menu(self):
        """Показує головне меню"""
        print("\n=== МЕНЮ ===")
        print("1. Парсити сайт")
        print("2. Показати всі дані")
        print("3. Вийти")

    def get_choice(self):
        """Отримує вибір користувача"""
        return input("Ваш вибір: ")


def run():
    db = DatabaseManager()
    parser = WebParser("https://example.com")
    ui = UserInterface()

    while True:
        ui.show_menu()
        choice = ui.get_choice()

        if choice == "1":
            data = parser.parse()
            for item in data:
                db.save_data(item)

        elif choice == "2":
            all_data = db.get_all_data()
            print("\n[DB] Усі дані:")
            for d in all_data:
                print("-", d)

        elif choice == "3":
            print("Вихід з програми...")
            break

        else:
            print("Невірний вибір! Спробуйте ще раз.")


if __name__ == "__main__":
    run()