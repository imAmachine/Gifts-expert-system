from models.CLI.ExpertMenu import ExpertMenu
from models.CLI.UserMenu import UserMenu
from models.ExpertEngine import ExpertEngine
from models.MenuItem import MenuItem
from models.menu import Menu
from tools.json_tools import load_json


def main():
    engine = ExpertEngine(rules=load_json('base/rules.json'), gifts=load_json('base/gifts.json'))

    # Menu items
    expert_menu_item = MenuItem('Эксперт', ExpertMenu(engine).show_menu)
    user_menu_item = MenuItem('Пользователь', UserMenu(engine).show_menu)

    # Main menu
    main_menu = Menu('ГЛАВНОЕ МЕНЮ')
    main_menu.add_item(expert_menu_item)
    main_menu.add_item(user_menu_item)

    # Start Menu
    main_menu.show_menu()


if __name__ == "__main__":
    main()
