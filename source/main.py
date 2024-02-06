import pygame
import initial_window
import main_game
pygame.init()

if __name__ == "__main__":
    # spouští úvodní obrazovku s nastavením
    initial_window.main()

    #ukládá kontrolu zda-li chceme dále pokračovat ve spouštění oken
    continue_running_check = initial_window.main()


    from initial_window import size

    if continue_running_check:

        main_game.main(size)
        from main_game import win

#   import scoreboard