from pyshortcuts import make_shortcut
from Card import Card
from Deck import Deck

fourdeck = Deck()
rows = 1
for x in range(1,3):
    for y in range(1,3):
        front = '{} x {}'.format(x, y)
        back = str(x * y)
        row = rows
        card = Card(front, back, row, rank=2, days=2)
        fourdeck.add_card(card)
        rows = rows + 1
fourdeck.new_day()        
fourdeck.cycle()
fourdeck.cycle()
fourdeck.cycle()

for x in range (0, len(fourdeck.all_cards)):
    if fourdeck.all_cards[x].miss > 1:
        print(fourdeck.all_cards[x].toString())
        print('You have missed this card before')

hard = fourdeck.hard_cards()
for x in range(0, len(hard)):
    print('hard')
