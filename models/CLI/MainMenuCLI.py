from models.CLI.CLI import CLI
from models.CLI.ExpertCLI import ExpertCLI
from models.CLI.UserCLI import UserCLI


class MainMenuCLI(CLI):
    def __init__(self, engine, title):
        super().__init__(engine, title)
        self.menu_items = self.__init_menu()
        self.title = title

    def __init_menu(self):
        choices = {
            'Пользователь': UserCLI(title='МЕНЮ ПОЛЬЗОВАТЕЛЯ', engine=self.engine, parent_cli=self).run_cli,
            'Эксперт': ExpertCLI(title='МЕНЮ ЭКСПЕРТА', engine=self.engine, parent_cli=self).run_cli
        }
        return choices
