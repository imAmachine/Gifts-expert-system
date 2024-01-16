from itertools import repeat

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

    def get_table(self):
        result_str_table = ''
        low_recommendation = [gift for gift in self if gift.rec_lvl == 0]
        med_recommendation = [gift for gift in self if gift.rec_lvl == 1]
        high_recommendation = [gift for gift in self if gift.rec_lvl == 2]

        lines_count = max(len(low_recommendation), len(med_recommendation), len(high_recommendation))
        col_width = max([len(gift.name) for gift in self]) + 2
        table_border_hor = ''.join(repeat('=', (col_width * 3) + 4)) +'\n'

        result_str_table += table_border_hor
        result_str_table += f"={'Подходят':^{col_width}}={'Подходят средне':^{col_width}}={'Подходят слабо':^{col_width}}=\n"
        result_str_table += table_border_hor

        for line in range(lines_count):
            h_r, m_r, l_r = '', '', ''
            if line < len(high_recommendation):
                h_r = high_recommendation[line].name

            if line < len(med_recommendation):
                m_r = med_recommendation[line].name

            if line < len(low_recommendation):
                l_r = low_recommendation[line].name

            result_str_table += f"={h_r:^{col_width}}={m_r:^{col_width}}={l_r:^{col_width}}=\n"
            result_str_table += table_border_hor

        return result_str_table
