from models.MenuItem import MenuItem
from models.menu import Menu
from tools.data_format import get_table_str


class ExpertMenu(Menu):
    def __init__(self, engine):
        super().__init__("МЕНЮ ЭКСПЕРТА")
        self.engine = engine
        self.add_item(MenuItem("Вывести список правил", action=self._struct_rules_output))
        self.add_item(MenuItem("Добавить правило", action=self._add_new_rule))
        self.add_item(MenuItem("Удалить правило по id", action=self._remove_rule))

    def _struct_rules_output(self):
        rules = self.engine.get_rules()

        id = [str(rule['id']) for rule in rules]
        property = [rule['property'] for rule in rules]
        values = [', '.join(rule['values']) for rule in rules]
        question = [rule['question'] for rule in rules]

        data = [id, property, values, question]
        headers = ['ID', 'Свойство', 'Значения', 'Вопрос']
        table_title = 'БАЗА ЗНАНИЙ'
        print(get_table_str(table_title, headers, data))

    def _add_new_rule(self):
        rule_id = input('Введите rule_id: ')
        if rule_id.isdigit():
            rule_id = int(rule_id)
            question = input('Введите вопрос: ')
            property = input('Введите имя свойства: ')
            values = [i.strip() for i in input('Введите значения (через запятую): ').split(',')]
            if len(values) > 0:
                self.engine.add_rule('./base/rules.json', rule_id, question, property, values)
                print('Правило успешно добавлено!')
            else:
                print('Некорректные данные! Количество значений не может быть меньше одного')
        else:
            print('Некорректные данные! rule_id должен быть числом')

    def _remove_rule(self):
        rule_id_str = input('Введите rule_id: ')
        if rule_id_str.isdigit():
            rule_id = int(rule_id_str)
            self.engine.remove_rule('./base/rules.json', rule_id)
            print(f'Правило с id {rule_id} успешно удалено!')
        else:
            print('Некорректные данные! rule_id должен быть числом')
