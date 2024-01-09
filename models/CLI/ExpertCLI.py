from models.CLI.CLI import CLI
from models.menu import Menu


class ExpertCLI(CLI):
    def __init__(self, title, engine, parent_menu):
        super().__init__(engine, parent_menu)
        self.engine = engine  # движок экспертной системы, с которым взаимодействует интерфейс
        self.menu = self.__init_menu(title, parent_menu)

    def __init_menu(self, title, parent_menu):
        choices = {
            "получить правила": self.__struct_rules_output,
            "добавить правила": self.__add_new_rule,
            "удалить правила": self.__remove_rule
        }
        return Menu(title, choices, parent_menu)

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
        self.engine.remove_rule(input('Введите id: '))