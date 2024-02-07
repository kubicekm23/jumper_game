import pygame
import initial_window
import main_game
pygame.init()

if __name__ == "__main__":
    #ukládá kontrolu zda-li chceme dále pokračovat ve spouštění oken
    from initial_window import main
    continue_running_check = main()


    from initial_window import chosen_character
    if continue_running_check:

        main_game.main(chosen_character)
        from main_game import win

#   import scoreboard