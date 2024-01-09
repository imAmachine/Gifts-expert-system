import json

import ExpertEngine
from menu import Menu


def load_json(path):
    try:
        with open(path, 'r', encoding="utf-8") as file:
            return json.load(file)
    except Exception as e:
        print(e)


def json_update(path, data):
    try:
        with open(path, 'w', encoding="utf-8") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
    except Exception as e:
        print(e)


def init_user_menu(engine, parent_menu):
    choices = {
        "Провести опрос": lambda: engine.load_ans_json('ans.json'),
        "Показать рекомендации": lambda: print(engine.get_recommendations())
    }
    return Menu(choices, parent_menu)


def init_expert_menu(engine, parent_menu):
    choices = {
        "получить правила": lambda: engine.get_rules(),
        "добавить правила": lambda:
            engine.add_rule(
                int(input('Введите id: ')),
                input('Введите вопрос: '),
                input('Введите имя свойства: '),
                [i.strip() for i in input('Введите значения (через запятую): ').split(',')]
            ),
        "удалить правила": lambda: engine.remove_rule(input('Введите id: ')),
    }
    return Menu(choices, parent_menu)


def init_main_menu(engine):
    choices = {
        'Пользователь': lambda: init_user_menu(engine, parent_menu).run_menu(),
        'Эксперт': lambda: init_expert_menu(engine, parent_menu).run_menu()
    }
    return Menu(choices)


if __name__ == "__main__":
    engine = ExpertEngine.ExpertEngine(rules=load_json('rules.json'), gifts=load_json('gifts.json'))
    parent_menu = init_main_menu(engine)
    parent_menu.run_menu()
