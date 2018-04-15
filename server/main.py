from engine import Engine
from print_engine import Engine_Print

def main():
    '''
        The whole source is developed on Python 3.6

        Engine:       using curses lib for realtime draw, the lib is in python-wheel package,
                      pip install python-wheel

        Engine_Print: using console print to draw the status, it didnt depent on other lib
    '''
    # game_engine = Engine_Print(20,20)
    game_engine = Engine(20,20)

    game_engine.run()
    game_engine.destroy()
    print('Game Over!')

if __name__ == '__main__':
    main()
