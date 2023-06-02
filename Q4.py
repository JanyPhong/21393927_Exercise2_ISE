'''
This program implements the Pocket Beast game. The game is played by two players.
'''


import random

def create_beasts():
    '''
    This function creates the beasts for the players.
    '''
      
    player_one_health = 50
    player_two_health = 50

    player_one_beast = input("Player 1, choose your beast: ")
    player_two_beast = input("Player 2, choose your beast: ")

    print("Player 1's beast is a " + player_one_beast)
    print("Player 2's beast is a " + player_two_beast)

    return player_one_health, player_two_health, player_one_beast, player_two_beast

def roll_dice(dice_type, dice_number):
    total = 0
    for _ in range(dice_number):
        total += random.randint(1, dice_type)
    return total


def perform_attack(attacker_beast, defender_beast, attacker_defending):
    if attacker_defending:
        print(f"{attacker_beast} is defending!")
    else:
        attacker_attack = roll_dice(6, 2)
        print(f"{attacker_beast} attacks {defender_beast} for {attacker_attack} damage")
        return attacker_attack

def play_game():
    player_one_health, player_two_health, player_one_beast, player_two_beast = create_beasts()
    while player_one_health > 0 and player_two_health > 0:
        print(f"{player_one_beast}'s health: {player_one_health}")
        print(f"{player_two_beast}'s health: {player_two_health}")
        
        player_one_defend = input("Player 1, do you want to defend? (y/n): ")
        player_one_attack = perform_attack(player_one_beast, player_two_beast, player_one_defend == "y")
        
        player_two_defend = input("Player 2, do you want to defend? (y/n): ")
        player_two_attack = perform_attack(player_two_beast, player_one_beast, player_two_defend == "y")
        
        player_one_health -= player_two_attack
        player_two_health -= player_one_attack

    return player_one_health, player_two_health, player_one_beast, player_two_beast


def print_winner(player_one_health, player_two_beast):
    if player_one_health <= 0:
        print(f"{player_two_beast} wins!")
    else:
        print("Player 1 wins!")


if __name__ == "__main__":
    player_one_health, player_two_health, player_one_beast, player_two_beast = play_game()
    print_winner(player_one_health, player_two_beast)
