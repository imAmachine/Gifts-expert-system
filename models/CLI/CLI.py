from models.menu import Menu


class CLI:
    def __init__(self, engine, title='МЕНЮ', parent_menu=None):
        self.engine = engine  # движок экспертной системы, с которым взаимодействует интерфейс
        self.menu = self.__init_menu(title, parent_menu)  # установка родительского меню

    def run_menu(self):
        self.menu.run_menu()  # старт основного цикла меню

    def __init_menu(self, title, parent_menu):
        choices = {}
        return Menu(title, choices, parent_menu=parent_menu)
