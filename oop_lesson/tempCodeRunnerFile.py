        print(40 * '-' + " Instructions: " + 40 * '-')
        print("All commands: 1. beat_damage  2. beat_healing")
        print("For command:  player.your-command(receiver-player)")
        print("See player health: print(player.get_health())")
        action = input("Make a decision: ")
        exec(action)