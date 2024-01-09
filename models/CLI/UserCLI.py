from models.CLI.CLI import CLI
from models.menu import Menu


class UserCLI(CLI):
    def __init__(self, title, engine, parent_menu):
        super().__init__(engine, title, parent_menu)
        self.menu = self.__init_menu(title, parent_menu)

    def __run_user_ask_method(self, method='ask'):
        if method == 'ask':
            self.engine.ask_user()
        elif method == 'load':
            self.engine.load_ans_json('./base/ans.json')

    def __show_recommendations(self):
        result = '\nВот список подарков, которые можно рассмотреть в качестве подарка:\n'
        recommendations = self.engine.get_recommendations()
        for idx, rec in enumerate(recommendations):
            result += f'{idx + 1} - {rec["name"]}\n'
        print(result)

    def __init_menu(self, title, parent_menu):
        choices = {
            "Провести опрос": lambda: self.__run_user_ask_method('load'),
            "Показать рекомендации": self.__show_recommendations
        }
        return Menu(title, choices, parent_menu)
