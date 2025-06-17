import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from windows.game_handler import main_menu_loop

def main():
    import cProfile
    import pstats

    profiler = cProfile.Profile()
    profiler.enable()
    try:
        main_menu_loop()
    except:
        pass

    profiler.disable()

    stats = pstats.Stats(profiler).sort_stats('tottime')
    stats.print_stats()


if __name__ == "__main__":
    main_menu_loop()
    #main()
