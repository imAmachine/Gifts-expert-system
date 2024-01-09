from models.CLI.CLI import CLI


class UserCLI(CLI):
    def __init__(self, title, engine, parent_cli):
        super().__init__(engine, title, parent_cli)
        self.menu_items = self.__init_menu()
        self.title = title
        self.parent_cli = parent_cli

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

    def __init_menu(self):
        choices = {
            "Провести опрос": lambda: self.__run_user_ask_method('load'),
            "Показать рекомендации": self.__show_recommendations
        }
        return choices
