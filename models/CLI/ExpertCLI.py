from models.CLI.CLI import CLI


class ExpertCLI(CLI):
    def __init__(self, engine, title, parent_cli):
        super().__init__(engine, title, parent_cli)
        self.engine = engine  # движок экспертной системы, с которым взаимодействует интерфейс
        self.menu_items = self.__init_menu()
        self.parent_cli = parent_cli
        self.title = title

    def __init_menu(self):
        choices = {
            "получить правила": self.__struct_rules_output,
            "добавить правила": self.__add_new_rule,
            "удалить правила": self.__remove_rule
        }
        return choices

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
        rule_id = int(input('Введите id: '))
        self.engine.remove_rule(rule_id)