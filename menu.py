import keyboard


class Menu:
    def __init__(self, menu_items: dict = None, parent_menu=None):
        self.menu_items = menu_items
        self.parent_menu = parent_menu

    def _display_menu(self):
        for idx, (item_name, _) in enumerate(zip(self.menu_items.keys(), self.menu_items.values()), start=1):
            print(f'{idx} - {item_name}')
        print('Нажмите ESC, чтобы выйти или вернуться на пункт выше.')
        print('Выберите пункт меню...')

    def _execute_item_action(self, action):
        if callable(action):
            action()
            self.run_menu()
        elif isinstance(action, Menu):
            action.parent_menu = self
            action.run_menu()

    def run_menu(self):
        self._display_menu()
        while True:
            key_event = keyboard.read_event(suppress=True)
            if key_event.event_type == keyboard.KEY_DOWN:
                if key_event.name.isdigit():
                    choice = int(key_event.name)
                    if 0 <= choice <= len(self.menu_items):
                        if choice == 0 and self.parent_menu is not None:
                            return
                        selected_item = list(self.menu_items.keys())[choice - 1]
                        action = self.menu_items[selected_item]
                        self._execute_item_action(action)
                    else:
                        print("Неверный выбор. Попробуйте еще раз.")
            elif key_event.name == 'esc':
                if self.parent_menu is not None:
                    self.parent_menu.run_menu()
                else:
                    exit()
