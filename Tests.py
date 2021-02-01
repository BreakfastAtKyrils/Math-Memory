from Card import Card
from Deck import Deck

fourdeck = Deck()
rows = 1
for x in range(1,3):
    for y in range(1,3):
        front = '{} x {}'.format(x, y)
        back = str(x * y)
        row = rows
        card = Card(front, back, row, rank=2, days=0)
        fourdeck.add_card(card)
        rows = rows + 1


fourdeck.cycle()
