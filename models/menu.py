class Menu:
    def __init__(self, title, items=None):
        self.title = title
        self.items = items or []

    def add_item(self, item):
        self.items.append(item)

    def show_menu(self):
        while True:
            print(f"\n{self.title}")
            for index, item in enumerate(self.items, start=1):
                print(f"{index}. {item.name}")

            choice = input("Выберите пункт меню (q - выход): ")
            if choice.lower() == 'q':
                break

            try:
                choice = int(choice)
                if 1 <= choice <= len(self.items):
                    selected_item = self.items[choice - 1]
                    selected_item.execute()
                else:
                    print("Некорректный выбор. Пожалуйста, выберите существующий пункт.")
            except ValueError:
                print("Введите число.")
