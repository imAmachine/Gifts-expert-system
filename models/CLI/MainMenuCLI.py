from models.CLI.CLI import CLI
from models.CLI.ExpertCLI import ExpertCLI
from models.CLI.UserCLI import UserCLI
from models.menu import Menu


class MainMenuCLI(CLI):
    def __init__(self, title, engine):
        super().__init__(engine)
        self.menu = self.__init_menu(title, None)

    def __init_menu(self, title, parent_menu):
        choices = {
            'Пользователь': UserCLI(title='МЕНЮ ПОЛЬЗОВАТЕЛЯ', engine=self.engine, parent_menu=self).run_menu,
            'Эксперт': ExpertCLI(title='МЕНЮ ЭКСПЕРТА', engine=self.engine, parent_menu=self).run_menu
        }
        return Menu(title, choices, parent_menu)
