from getpass import getpass as input

# Define ANSI escape codes for colors
GREEN = "\033[32m"
RED = "\033[31m"
BLUE = "\033[34m"
RESET = "\033[0m"

# Helper function to determine if player1 wins
def player1_wins(p1, p2):
    return (p1 == "R" and p2 == "S") or (p1 == "P" and p2 == "R") or (p1 == "S" and p2 == "P")

print(f"{BLUE}Let's play Rock, Paper, Scissors{RESET}")
print()

scoreP1 = 0
scoreP2 = 0

while True:
    print("\nPlayers, select your move (R, P, or S)")
    player1 = input(f"{GREEN}\nPlayer 1 > {RESET}")
    player2 = input(f"{RED}\nPlayer 2 > {RESET}")
    player1 = player1.upper()
    player2 = player2.upper()

    if player1 == player2:
        print(f"{BLUE}\nIt's a tie.{RESET}")
        print(f"{BLUE}No points for anyone!{RESET}")
    elif player1_wins(player1, player2):
        print(f"{GREEN}\nPlayer 1 wins!{RESET}")
        scoreP1 += 1
    elif player1_wins(player2, player1):
        print(f"{RED}\nPlayer 2 wins!{RESET}")
        scoreP2 += 1
    else:
        if player1 not in ["R", "P", "S"]:
            print(f"{GREEN}\nInvalid move Player 1!{RESET}")
        if player2 not in ["R", "P", "S"]:
            print(f"{RED}\nInvalid move Player 2!{RESET}")
        break

    # Display the updated scores
    print(f"{GREEN}\nPlayer 1 has {scoreP1} points{RESET}")
    print(f"{RED}\nPlayer 2 has {scoreP2} points{RESET}")

    # Check for game over conditions
    if scoreP1 == 3:
        print(f"{GREEN}\nPlayer 1 wins! Game over for Player 2.{RESET}")
        break
    elif scoreP2 == 3:
        print(f"{RED}\nPlayer 2 wins! Game over for Player 1.{RESET}")
        break
