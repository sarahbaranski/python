"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    if card == "J" or card == "K" or card == "Q":
       return 10
    elif card == "A":
       return 1
    return int(card)
    


def higher_card(card_one, card_two):
   value_1 = value_of_card(card_one)
   value_2 = value_of_card(card_two)
   if value_1 > value_2:
       return card_one
   elif value_2 > value_1:
       return card_two
   return card_one, card_two


def value_of_ace(card_one, card_two):
    if card_one == "A" or card_two == "A":
        return 1
    elif value_of_card(card_one) + value_of_card(card_two) <= 10:
        return 11
    else:
        return 1


def is_blackjack(card_one, card_two):
    total_value = value_of_card(card_one) + value_of_card(card_two)

    if card_one == "A" or card_two == "A":
        return total_value == 11
    return total_value == 21


def can_split_pairs(card_one, card_two):
    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one, card_two):
    total = value_of_card(card_one) + value_of_card(card_two)
    return total >= 9 and total <= 11
