import ExpertEngine
from UserCLI import MainMenuCLI
from json_tools import load_json


if __name__ == "__main__":
    engine = ExpertEngine.ExpertEngine(rules=load_json('rules.json'), gifts=load_json('gifts.json'))
    cli = MainMenuCLI(engine=engine)
    cli.run_menu()