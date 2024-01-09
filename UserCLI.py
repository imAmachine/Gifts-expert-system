from menu import Menu


class CLI:
    def __init__(self, engine, parent_menu=None):
        self.engine = engine  # движок экспертной системы, с которым взаимодействует интерфейс
        self.menu = self.__init_menu()  # установка родительского меню

    def start_cli(self):
        self.menu.run_menu()  # старт основного цикла меню

    def __init_menu(self):
        return Menu()


class MainMenuCLI(CLI):
    def __init__(self, engine):
        super().__init__(engine)
        self.menu = self.__init_menu()

    def __init_menu(self):
        choices = {
            'Пользователь': UserCLI(engine=self.engine, parent_menu=self).start_cli,
            'Эксперт': ExpertCLI(engine=self.engine, parent_menu=self).start_cli
        }
        return Menu(choices, self.menu)


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


class ExpertCLI(CLI):
    def __init__(self, engine, parent_menu):
        super().__init__(engine, parent_menu)
        self.engine = engine  # движок экспертной системы, с которым взаимодействует интерфейс
        self.menu = self.__init_expert_menu(parent_menu)

    def __init_expert_menu(self, parent_menu):
        choices = {
            "получить правила": self.__struct_rules_output,
            "добавить правила": self.__add_new_rule,
            "удалить правила": self.__remove_rule
        }
        return Menu(choices, parent_menu)

    def __struct_rules_output(self):
        print('id - property - values - question\n' + '\n'.join(self.engine.get_rules()))

    def __add_new_rule(self):
        self.engine.add_rule(
            int(input('Введите id: ')),
            input('Введите вопрос: '),
            input('Введите имя свойства: '),
            [i.strip() for i in input('Введите значения (через запятую): ').split(',')]
        )

    def __remove_rule(self):
        self.engine.remove_rule(input('Введите id: ')),