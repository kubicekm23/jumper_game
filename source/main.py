if __name__ == "__main__":
    from initial_window import main

    returned_values = main()

    # uložení kontroly zda-li chceme nadále hrát
    continue_running_check = returned_values[0]
    # uložení vybrané postavy
    chosen_character = returned_values[1]
    # uložení jména hráče
    player_name = returned_values[2]

    if continue_running_check:
        import first_level
        returned_values = first_level.main(chosen_character)

        win_check = returned_values[0]
        time_played = returned_values[1]
        continue_running_check = returned_values[2]

        # výpočet času
        seconds = (time_played / 1000) % 60
        seconds = int(seconds)
        minutes = (time_played / (1000 * 60)) % 60
        minutes = int(minutes)

        if continue_running_check:
            from scoreboard import main
            main(minutes, seconds, player_name, win_check)