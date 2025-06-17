import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from windows.game_handler import main_menu_loop


if __name__ == "__main__":
    main_menu_loop()
