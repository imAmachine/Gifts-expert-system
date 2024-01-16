class RecommendationItem:
    def __init__(self, gift_name: str, prop_passed: int, prop_count: int):
        self.name = gift_name
        self.rec_lvl = self._calc_rec_lvl(prop_passed, prop_count)

    def _calc_rec_lvl(self, prop_passed, prop_count):
        """Уровень рекомендации (от -1 до 2, где
        2 - подходит,
        1 - средне подходит
        0 - слабо подходит
        -1 - не подходит)"""
        calculated = round((100 * prop_passed) / prop_count)

        if 0 <= calculated < 50:
            return -1
        if 50 <= calculated < 70:
            return 0
        if 70 <= calculated < 100:
            return 1
        return 2