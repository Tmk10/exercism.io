# Score categories
# Change the values as you see fit

ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = "Full House"
FOUR_OF_A_KIND = "Four of a kind"
LITTLE_STRAIGHT = "Little straight"
BIG_STRAIGHT = "Big straight"
CHOICE = "Choice"
YACHT = "Yacht"


def score(dice, category):
    dice.sort()

    if category in [ONES, TWOS, THREES, FOURS, FIVES, SIXES]:
        return dice.count(category) * category

    elif category == FULL_HOUSE:
        if len(set(dice)) == 1 or len(set(dice)) > 2 or 4 in [dice.count(score) for score in dice]:
            return 0
        return sum(dice)

    elif category == FOUR_OF_A_KIND:
        if 1 <= len(set(dice)) > 2:
            return 0
        return dice[2] * 4

    elif category == LITTLE_STRAIGHT:
        if len(set(dice)) != 5 or sum(dice) != 15:
            return 0
        return 30

    elif category == BIG_STRAIGHT:
        if len(set(dice)) != 5 or sum(dice) != 20:
            return 0
        print(sum(dice))
        return 30

    elif category == CHOICE:
        return sum(dice)

    elif category == YACHT:
        if len(set(dice)) != 1:
            return 0
        return 50



print(score([1, 1, 3, 4, 5], LITTLE_STRAIGHT))

