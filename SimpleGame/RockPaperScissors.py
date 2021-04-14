import random


# Build s simple Rock paper Scissor game.
# A player who decides to play rock will beat another player who has chosen scissors
# ("rock crushes scissors" or sometimes "blunts scissors"), but will lose
# to one who has played paper ("paper covers rock"); a play of paper will lose to a play of
# scissors ("scissors cuts paper").


def play_game(a, b):
    if a == b:
        return "Draw game", None
    #   winning tuples
    winning_combinations = (
        ("rock", "scissor"),
        ("paper", "rock"),
        ("scissor", "paper")
    )
    winning_reason = (
        "rock smashes scissor",
        "paper covers rock",
        "scissor cuts paper"
    )
    if (a, b) in winning_combinations:
        return "You win", winning_reason[winning_combinations.index((a, b))]
    return "Computer wins", None


try:
    allowed_options = ["rock", "paper", "scissor"]
    player = input("Let's play. Pick <rock, paper, scissor> : ")
    if player not in allowed_options:
        raise ValueError("Invalid option entered")
    pc = random.choice(allowed_options)
    print("You picked : " + player)
    print("PC picked  : " + pc)
    winner, reason = play_game(player, pc)
    print("Game result : ", winner)
    if reason:
        print(reason)

except ValueError as err:
    print(err)
