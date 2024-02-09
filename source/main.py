import pygame
pygame.init()

if __name__ == "__main__":
    from initial_window import main

    returned_values = main()

    # uložení kontroly zda-li chceme nadále hrát
    continue_running_check = returned_values[0]
    # uložení vybrané postavy
    chosen_character = returned_values[1]

#    if continue_running_check:
#
#        import main_game
#        main_game.main(chosen_character)
#        from main_game import win, time_spent
#        returned_values = main()

    if continue_running_check:
        import main_game
        main_game.main(chosen_character)

        from main_game import win, time_spent
        returned_values = main_game.main(chosen_character)
        win_check = returned_values[0]
        time_spent_playing = returned_values[1]

        print(win_check, time_spent_playing)

    #import scoreboard
