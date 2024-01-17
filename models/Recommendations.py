from models.rec_item import RecommendationItem


class Recommendations(list):
    def __init__(self, rules_list, gifts_list, user_answers):
        super().__init__()
        self._init_recommendations(rules_list, gifts_list, user_answers)

    def _init_recommendations(self, rules_list, gifts_list, user_answers):
        if user_answers:
            for gift in gifts_list:
                rules_checked = []
                rules_by_gift = [rule for rule in rules_list if rule["property"] in gift["properties"]]
                gift_properties = gift["properties"]

                for rule in rules_by_gift:
                    rule_property_name = rule["property"]
                    gift_property_value = gift_properties[rule_property_name]

                    user_answer_value = user_answers[rule_property_name]
                    rules_checked.append(gift_property_value == user_answer_value)
                rules_passed = [rule_status for rule_status in rules_checked if rule_status]
                rec_item = RecommendationItem(gift["name"], len(rules_passed), len(gift_properties))
                self.append(rec_item)