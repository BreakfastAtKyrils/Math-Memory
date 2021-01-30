from datetime import date
import csv
from Card import Card

# the following is the User class


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# The following is the Deck class, which will hold a list of Cards
# It assumes the card class has been instanciated




deck = Deck()

# this loop creates a deck of 144 cards for each multiplication in the 1-12 table
for x in range(1, 2):
    for y in range(1, 2):
        front = '{} x {}'.format(x, y)
        back = x * y
        card = Card(front, back, row = 1, rank=1, days=0)
        deck.add_card(card)


print('this is BEFORE we play')
deck.make_csv()
deck.show_rows()
deck.play()

print('this is AFTER we play')
deck.make_csv()
deck.show_rows()

print('this is the following day: ')
deck.new_day()
deck.new_day()
deck.new_day()
deck.show_rows()

print('we play the following day: ')
deck.play()
deck.show_rows()


