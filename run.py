from models import ExpertEngine
from models.CLI.MainMenuCLI import MainMenuCLI
from tools.json_tools import load_json


if __name__ == "__main__":
    engine = ExpertEngine.ExpertEngine(rules=load_json('base/rules.json'), gifts=load_json('base/gifts.json'))
    cli = MainMenuCLI(engine=engine)
    cli.run_menu()