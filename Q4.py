'''
This program implements the Pocket Beast game. The game is played by two players.
'''


import random

def create_beasts():
    '''
    This function creates the beasts for the players.
    '''
    global player_one_health
    global player_two_health   
    global player_one_beast
    global player_two_beast 
      
    player_one_health = 50
    player_two_health = 50

    player_one_beast = input("Player 1, choose your beast: ")
    player_two_beast = input("Player 2, choose your beast: ")

    print("Player 1's beast is a " + player_one_beast)
    print("Player 2's beast is a " + player_two_beast)


def attack(dice_type, dice_number, is_defending):
    '''
    This function simulates an attack by rolling the dice and returning the total 
    unless the beast is defending then it does nothing
    '''
    total = 0
    if is_defending:
        print("Defending!")
    else:
        for _ in range(dice_number):
            total = total + random.randint(1, dice_type)
    return total


def print_attack_message(player_one_beast, player_one_attack, player_two_beast, player_two_attack, current_player):
    '''
    This function prints the attack message for the provided player
    '''
    if current_player == 1:
        print(f"{player_one_beast} attacks {player_two_beast} for {player_one_attack} damage")
    elif current_player == 2:
        print(f"{player_two_beast} attacks {player_one_beast} for {player_two_attack} damage")

def play_game():
    global player_one_health
    global player_two_health
    while player_one_health > 0 and player_two_health > 0:
        print(f"{player_one_beast}'s health: {player_one_health}")
        print(f"{player_two_beast}'s health: {player_two_health}")
        player_one_defend = input("Player 1, do you want to defend? (y/n): ")
        player_two_defend = input("Player 2, do you want to defend? (y/n): ")
        if player_one_defend == "y":
            player_one_attack = attack(6, 2, True)
        else:
            player_one_attack = attack(6, 2, False)

        if player_two_defend == "y":
            player_two_attack = attack(6, 2, True)
        else:
            player_two_attack = attack(6, 2, False)
        
        player_one_health = player_one_health - player_two_attack
        player_two_health = player_two_health - player_one_attack
        print_attack_message(player_one_beast, player_one_attack, player_two_beast, player_two_attack, 1)
        print_attack_message(player_one_beast, player_one_attack, player_two_beast, player_two_attack, 2)

def print_winner():
    '''
    This function prints the winner of the game
    '''
    if player_one_health <= 0:
        print(f"{player_two_beast} wins!")
    else:
        print(f"{player_one_beast} wins!")


if __name__ == "__main__":
    create_beasts()
    play_game()
    print_winner()