from models.CLI.MenuItem import MenuItem
from models.menu import Menu


class ExpertMenu(Menu):
    def __init__(self, engine):
        super().__init__("МЕНЮ ЭКСПЕРТА")
        self.engine = engine
        self.add_item(MenuItem("Вывести список правил", action=self._struct_rules_output))
        self.add_item(MenuItem("Добавить правило", action=self._add_new_rule))
        self.add_item(MenuItem("Удалить правило по id", action=self._remove_rule))

    def _struct_rules_output(self):
        print('id - property - values - question\n' + '\n'.join(self.engine.get_rules()))

    def _add_new_rule(self):
        self.engine.add_rule(
            int(input('Введите id: ')),
            input('Введите вопрос: '),
            input('Введите имя свойства: '),
            [i.strip() for i in input('Введите значения (через запятую): ').split(',')]
        )

    def _remove_rule(self):
        rule_id = int(input('Введите id: '))
        self.engine.remove_rule(rule_id)
