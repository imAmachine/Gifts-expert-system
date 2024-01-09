from models.menu import Menu


class CLI:
    def __init__(self, engine, parent_menu=None):
        self.engine = engine  # движок экспертной системы, с которым взаимодействует интерфейс
        self.menu = self.__init_menu()  # установка родительского меню

    def run_menu(self):
        self.menu.run_menu()  # старт основного цикла меню

    def __init_menu(self):
        choices = {}
        return Menu(choices, parent_menu=None)
