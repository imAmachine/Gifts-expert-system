from models.Recommendations import Recommendations
from tools.json_tools import json_update, load_json


class ExpertEngine:
    def __init__(self, gifts, rules):
        self._UserAnswers = None
        self._gifts = gifts
        self._rules = rules

    def ask_user(self) -> None:
        # self._UserAnswers = load_json(r"F:\Downloads\ans.json")
        self._UserAnswers = dict()
        for rule in self._rules:
            while True:
                question = rule["question"]
                values = '\n'.join([f'{idx + 1} - {val}' for idx, val in enumerate(rule["values"])])
                print(question + '\n' + values)

                ans = int(input())
                if 0 < ans <= len(rule["values"]):
                    if rule["values"][ans-1] in rule["values"]:
                        self._UserAnswers.update({rule["property"]: rule["values"][ans-1]})
                        break
                else:
                    print('Такого пункта не существует, попробуйте ещё раз')

    def get_recommendations(self) -> list:
        if self._UserAnswers:
            return Recommendations(self._rules, self._gifts, self._UserAnswers)
        else:
            return None

    def get_rules(self) -> list:
        """метод для получения списка правил в базе знаний"""
        result = list()
        for rule in self._rules:
            rule_id = rule['id']
            property_name = rule['property']
            values = rule['values']
            question = rule['question']
            rule_line = f'{rule_id} - {property_name} - {values} - {question}'
            result.append(rule_line)
        return result

    def remove_rule(self, rules_path, rule_id) -> bool:
        """Метод для удаления правила по id"""
        new_rules_list = [rule for rule in self._rules if rule["id"] != rule_id]
        self._rules = new_rules_list
        return json_update(rules_path, self._rules)

    def add_rule(self, rules_path, rule_id: int, question: str, property_name: str, values: list) -> bool:
        """метод для добавления нового правила"""
        new_rule = {
            "id": rule_id,
            "property": property_name,
            "values": values,
            "question": question
        }

        self._rules.append(new_rule)
        return json_update(rules_path, self._rules)
