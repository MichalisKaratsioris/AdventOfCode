"""
--- Day 2: Rock Paper Scissors ---

--- Part One ---
The Elves begin to set up camp on the beach. To decide whose tent gets to be closest to the snack storage, a giant
Rock Paper Scissors tournament is already in progress.

Rock Paper Scissors is a game between two players. Each game contains many rounds; in each round, the players each
simultaneously choose one of Rock, Paper, or Scissors using a hand shape. Then, a winner for that round is selected:
    - Rock defeats Scissors,
    - Scissors defeats Paper, and
    - Paper defeats Rock.
If both players choose the same shape, the round instead ends in a draw.

Appreciative of your help yesterday, one Elf gives you an encrypted strategy guide (your puzzle input) that they say
will be sure to help you win. "The first column is what your opponent is going to play: A for Rock, B for Paper, and C
for Scissors. The second column--" Suddenly, the Elf is called away to help with someone's tent.

The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors.
Winning every time would be suspicious, so the responses must have been carefully chosen.

The winner of the whole tournament is the player with the highest score. Your total score is the sum of your scores for
each round. The score for a single round is the score for the shape you selected
(1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round
(0 if you lost, 3 if the round was a draw, and 6 if you won).

Since you can't be sure if the Elf is trying to help you or trick you, you should calculate the score you would get
if you were to follow the strategy guide.

For example, suppose you were given the following strategy guide:

                                A Y
                                B X
                                C Z

This strategy guide predicts and recommends the following:

In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). This ends in a win for you
with a score of 8 (2 because you chose Paper + 6 because you won).
In the second round, your opponent will choose Paper (B), and you should choose Rock (X). This ends in a loss for you
with a score of 1 (1 + 0).
The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.
In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).

What would your total score be if everything goes exactly according to your strategy guide?
"""
import os


def rock_paper_scissors_21(s: str) -> int:
    """

    """

    dir_path = os.path.dirname(os.path.abspath(__file__))
    txt_file = os.path.join(dir_path, s)

    with open(txt_file, mode='a') as f:
        f.write("\n\n")

    points = 0
    shapes = {
        "A X\n": 4,
        "A Y\n": 8,
        "A Z\n": 3,
        "B X\n": 1,
        "B Y\n": 5,
        "B Z\n": 9,
        "C X\n": 7,
        "C Y\n": 2,
        "C Z\n": 6
    }
    with open(txt_file, mode='r') as f:
        for line in f:
            if line in shapes.keys():
                points = points + shapes[line]
    return points


# print(rock_paper_scissors_21('test.txt'))
# print(rock_paper_scissors_21('input_day_2.txt'))


"""
Your puzzle answer was 12458. The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---
The Elf finishes helping with the tent and sneaks back over to you. "Anyway, the second column says how the round 
needs to end: X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. 
Good luck!"

The total score is still calculated in the same way, but now you need to figure out what shape to choose so the round 
ends as indicated. The example above now goes like this:

In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y), so you also choose 
Rock. This gives you a score of 1 + 3 = 4.
In the second round, your opponent will choose Paper (B), and you choose Rock so you lose (X) with a score of 1 + 0 = 1.
In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.
Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of 12.

Following the Elf's instructions for the second column, what would your total score be if everything goes exactly 
according to your strategy guide?
"""


def rock_paper_scissors_22(s: str) -> int:
    """

    """

    dir_path = os.path.dirname(os.path.abspath(__file__))
    txt_file = os.path.join(dir_path, s)

    with open(txt_file, mode='a') as f:
        f.write("\n\n")

    points = 0
    with open(txt_file, mode='r') as f:
        for line in f:
            if line[0] == "A":
                if line[2] == "X":
                    points = points + 3
                if line[2] == "Y":
                    points = points + 4
                if line[2] == "Z":
                    points = points + 8
            if line[0] == "B":
                if line[2] == "X":
                    points = points + 1
                if line[2] == "Y":
                    points = points + 5
                if line[2] == "Z":
                    points = points + 9
            if line[0] == "C":
                if line[2] == "X":
                    points = points + 2
                if line[2] == "Y":
                    points = points + 6
                if line[2] == "Z":
                    points = points + 7
    return points


# print(rock_paper_scissors_22('test.txt'))
# print(rock_paper_scissors_22('input_day_2.txt'))

"""
Your puzzle answer was 12683. Both parts of this puzzle are complete! They provide two gold stars: **
You are two gold stars closer to collecting enough star fruit. You have completed Day 2!
"""
