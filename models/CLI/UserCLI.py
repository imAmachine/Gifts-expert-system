from models.CLI.CLI import CLI
from models.menu import Menu


class UserCLI(CLI):
    def __init__(self, engine, parent_menu):
        super().__init__(engine, parent_menu)
        self.menu = self.__init_user_menu(parent_menu)

    def __run_user_ask_method(self, method='ask'):
        if method == 'ask':
            self.engine.ask_user()
        elif method == 'load':
            self.engine.load_ans_json('ans.json')

    def __show_recommendations(self):
        print(self.engine.get_recommendations())

    def __init_user_menu(self, parent_menu):
        choices = {
            "Провести опрос": self.__run_user_ask_method('load'),
            "Показать рекомендации": self.__show_recommendations
        }
        return Menu(choices, parent_menu)