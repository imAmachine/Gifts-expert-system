import keyboard


class CLI:
    def __init__(self, engine, title='МЕНЮ', parent_cli=None):
        self.engine = engine  # движок экспертной системы, с которым взаимодействует интерфейс
        self.parent_cli = parent_cli
        self.title = title
        self.menu_items = self.__init_menu()

    def _display(self):
        print(f'\n=========={self.title}==========')
        for idx, (item_name, _) in enumerate(zip(self.menu_items.keys(), self.menu_items.values()), start=1):
            print(f'{idx} - {item_name}')
        print('ESC - чтобы вернуться назад')
        print('Выберите пункт меню...')

    def _execute_item_action(self, action):
        if callable(action):
            action()
            self.run_cli()
        elif isinstance(action, CLI):
            action.parent_cli = self
            action.run_cli()

    def run_cli(self):
        self._display()
        while True:
            key_event = keyboard.read_event(suppress=True)
            if key_event.event_type == keyboard.KEY_DOWN:
                if key_event.name.isdigit():
                    choice = int(key_event.name)
                    if 0 <= choice <= len(self.menu_items):
                        selected_item = list(self.menu_items.keys())[choice - 1]
                        action = self.menu_items[selected_item]
                        self._execute_item_action(action)
                        return
            elif key_event.name == 'esc':
                return

    def __init_menu(self):
        choices = {}
        return choices
