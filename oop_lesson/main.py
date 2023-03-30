from hero import Hero
from orc import Orc
from assasin import Assasin
from healer import Healer
from weapon import Weapon
from entity import Entity

if __name__ == "__main__":
    all_players = []
    die_players = []
    
    bad = Orc("Joker", 74, 1)
    nunchaku = Weapon("Nunchaku", 10, 0.6)
    bad.equip_weapon(nunchaku)
    all_players.append(bad)
    
    healer = Healer("Pavlin", 36, "Poco", 10)
    shuriken = Weapon("Shuriken", 5, 0.7)
    healer.equip_weapon(shuriken)
    all_players.append(healer)
    
    assasin = Assasin("Gosho", 53, "Burziqt")
    sword = Weapon("Sword", 15, 0.4)
    assasin.equip_weapon(sword)
    all_players.append(assasin)
    
    
    while 1:
        # bad.beat_damage(assasin)
        # print(assasin.get_health())
        # healer.beat_healing(assasin)
        # print(assasin.get_health())
        # healer.beat_damage(bad)
        # print(bad.get_health())
        # assasin.beat_damage(3, bad)
        # print(bad.get_health())
        print(40 * '-' + " Instructions: " + 40 * '-')
        print("All commands: 1. beat_damage  2. beat_healing")
        print("For command:  player.your-command(receiver-player)")
        print("See player health: print(player.get_health())")
        action = input("Make a decision: ")
        exec(action)
        
        die_count = 0
        for player in all_players:
            if not player.is_alive():
                die_players.append(player)
                die_count += 1
       
        die_players = set(die_players) 
        all_players = [dif_player for dif_player in all_players if dif_player not in die_players]
        
        if die_count > 1:
            print(f"{all_players[0]} is winner!")
            break