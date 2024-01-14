from models.CLI.MenuItem import MenuItem
from models.menu import Menu


class UserMenu(Menu):
    def __init__(self, engine):
        super().__init__("МЕНЮ ПОЛЬЗОВАТЕЛЯ")
        self.engine = engine
        self.add_item(MenuItem("Провести опрос", action=self._run_user_ask_method))
        self.add_item(MenuItem("Получить рекомендации", action=self._show_recommendations))

    def _run_user_ask_method(self):
        self.engine.ask_user()

    def _show_recommendations(self):
        result = '\nВот список подарков, которые можно рассмотреть в качестве подарка:\n'
        recommendations = self.engine.get_recommendations()
        for idx, rec in enumerate(recommendations):
            result += f'{idx + 1} - {rec["name"]}\n'
        print(result)
