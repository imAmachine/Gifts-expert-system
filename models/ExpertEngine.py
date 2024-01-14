from tools.json_tools import load_json, json_update


class ExpertEngine:
    def __init__(self, gifts, rules):
        self._UserAnswers = None
        self._gifts = gifts
        self._rules = rules

    def ask_user(self) -> None:
        self._UserAnswers = dict()
        for rule in self._rules["rules"]:
            while True:
                question = rule["question"]
                values = '\n'.join([f'{idx + 1} - {val}' for idx, val in enumerate(rule["values"])])
                print(question + '\n' + values)

                ans = int(input())
                if 0 < ans <= len(rule["values"]):
                    if rule["values"][ans-1] in rule["values"]:
                        self._UserAnswers.update({rule["property"]: ans})
                        break
                else:
                    print('Такого пункта не существует, попробуйте ещё раз')

    def get_recommendations(self) -> list:
        recommendations = []

        if self._UserAnswers:
            for gift in self._gifts["gifts"]:
                accepted_rules = []
                gifts_rules_ids = gift["rules_id"]

                for rule in [rule for rule in self._rules["rules"] if rule["id"] in gifts_rules_ids]:
                    gift_property = gift["properties"][rule["property"]]
                    user_answer = self._UserAnswers["answers"][rule["property"]]
                    accepted_rules.append(gift_property == user_answer)

                if all(accepted_rules):
                    recommendations.append(gift)

        return recommendations

    def get_rules(self) -> list:
        result = list()
        for rule in self._rules["rules"]:
            rule_id = rule['id']
            property_name = rule['property']
            values = rule['values']
            question = rule['question']
            rule_line = f'{rule_id} - {property_name} - {values} - {question}'
            result.append(rule_line)
        return result

    def remove_rule(self, id_to_remove) -> bool:
        new_rules_list = [rule for rule in self._rules["rules"] if rule["id"] != id_to_remove]
        self._rules["rules"] = new_rules_list
        return json_update('./base/rules.json', self._rules)

    def add_rule(self, rule_id: int, question: str, property_name: str, values: list) -> bool:
        new_rule = {
            "id": rule_id,
            "property": property_name,
            "values": values,
            "question": question
        }

        self._rules["rules"].append(new_rule)
        return json_update('./base/rules.json', self._rules)
