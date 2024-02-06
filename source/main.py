import pygame
pygame.init()

if __name__ == "__main__":
    # spouští úvodní obrazovku s nastavením
    import initial_window

    #ukládá kontrolu zda-li chceme dále pokračovat ve spouštění oken
    from initial_window import continue_running_check
    print(continue_running_check)

    if continue_running_check:
        import main_game
        from main_game import win

#    if win:
#        import scoreboard