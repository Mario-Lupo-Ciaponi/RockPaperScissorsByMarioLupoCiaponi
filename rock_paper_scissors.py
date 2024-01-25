import random

print("========== Log in ==========")
username = input("Please type your player name: ")

print()
print("========== Rules ==========")
print(f"Welcome, {username} to the rock-paper-scissors game!")
print("The rules are pretty simple: rock beats scissors, scissors beat paper and paper beats rock.\n")

print("========== Selecting a gamemode ==========")
print("Available gamemods: \n1. One win game(the players who wins the first match, wins the entire game\n"
      "2. Several wins(you will chose the number of won matches necessary to win the game)\n")

gamemode = int(input("Please select the number of gamemode you want to play: "))
number_of_matches_for_win = 0  # This variable will store the wins necessary to win the whole game
while True:
    if gamemode == 1:
        print(f"{username}, selected the 'One win game' gamemode.")
        number_of_matches_for_win = 1
    elif gamemode == 2:
        print(f"{username}, selected the 'Several wins' gamemode.")
        number_of_matches_for_win = int(input("Please select the number of wins necessary to win the whole game"))
    else:
        gamemode = int(input("Invalid gamemode! Please reselect the number of gamemode you want to play: "))
        continue

    break
print()

player_one_wins = 0
player_two_wins = 0
draws = 0

winner_name = 0
choices = "rps"

number_of_matches = 1

while True:
    print(f"========== Match-{number_of_matches} ==========")
    player_one_move = input("Please type the first letter of the move you want to make(e.g. s(scissors)): ")
    player_two_move = random.choice(choices)

    if player_one_move == "r":
        if player_two_move == "s":
            player_one_wins += 1
        elif player_two_move == "p":
            player_two_wins += 1
        else:
            draws += 1
    elif player_one_move == "p":
        if player_two_move == "s":
            player_two_wins += 1
        elif player_two_move == "r":
            player_one_wins += 1
        else:
            draws += 1
    elif player_one_move == "s":
        if player_two_move == "p":
            player_one_wins += 1
        elif player_two_move == "r":
            player_two_wins += 1
        else:
            draws += 1

    if player_one_wins == number_of_matches_for_win:
        winner_name = username
        break
    elif player_two_wins == number_of_matches_for_win:
        winner_name = "Player-2"
        break

    number_of_matches += 1

print()
print("========== Result ==========")
print(f"{winner_name} won the game of Rock-Paper-Scissors! Congratulation!\n")
print(f"{username} wins: {player_one_wins} \nPlayer two wins: {player_two_wins} \nDraws: {draws}")
