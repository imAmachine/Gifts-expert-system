from models.CLI.CLI import CLI
from models.CLI.ExpertCLI import ExpertCLI
from models.CLI.UserCLI import UserCLI
from models.menu import Menu


class MainMenuCLI(CLI):
    def __init__(self, engine):
        super().__init__(engine)
        self.menu = self.__init_menu()

    def __init_menu(self):
        choices = {
            'Пользователь': UserCLI(engine=self.engine, parent_menu=self).run_menu,
            'Эксперт': ExpertCLI(engine=self.engine, parent_menu=self).run_menu
        }
        return Menu(choices, None)