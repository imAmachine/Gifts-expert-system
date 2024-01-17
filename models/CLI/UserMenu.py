from models.MenuItem import MenuItem
from models.menu import Menu


class UserMenu(Menu):
    def __init__(self, engine, answers_path):
        super().__init__("МЕНЮ ПОЛЬЗОВАТЕЛЯ")
        self.engine = engine
        self.add_item(MenuItem("Провести опрос", action=self._run_user_ask_method))
        self.add_item(MenuItem("Загрузить ответы из файла", action=lambda: self._run_file_loading(answers_path)))
        self.add_item(MenuItem("Получить рекомендации", action=self._show_recommendations))

    def _run_user_ask_method(self):
        """метод взаимодействия с движком ЭС, который запускает опрос пользователя"""
        self.engine.ask_user()

    def _run_file_loading(self, path):
        self.engine.load_ans_from_json(path)

    def _show_recommendations(self):
        """метод взаимодействия с движком ЭС, который выводит рекомендации для пользователя по проведённому опросу"""
        recommendations = self.engine.get_recommendations()
        print(recommendations.get_table())
