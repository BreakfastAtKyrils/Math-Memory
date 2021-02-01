import csv
class Deck:
    # all_cards will hold all the cards
    # file name for the .csv file

    def __init__(self):
        self.all_cards = []
        self.file_name = 'cards_list.csv'

    # this method takes the full deck, check whether days = 0 -> appends to review_deck
    def create_review_deck(self):
        review_deck = [card for card in self.all_cards if card.days == 0]
        return review_deck

     # adds a new card to the deck
    def add_card(self, card):
        self.all_cards.append(card)
        self.make_csv()

    # this method reviews today's deck by asking user each question
    # it assumes the create_review_deck() method has been called
    def review(self, deck):
        for x in range(0, len(deck)):
            question = deck[x].front
            answer = input('Question: ' + question)
            result = deck[x].check(answer)
            deck[x].update(result)
        self.make_csv()

    # this is the method that decrements 1 every night at midnight from the days attribute
    def new_day(self):
        for x in range(0, len(self.all_cards)):
            if self.all_cards[x].days >= 1:
                self.all_cards[x].days -= 1
            elif self.all_cards[x].days < 1:
                self.all_cads[x] = 0
        self.make_csv()

    # this method is called everytime there is a change to the Deck, it refreshes
    # the csv file to be up to date    
    def make_csv(self):
        #this resets the csv file to its original blank state
        data = open('cards_list.csv', mode = 'w', newline='')
        #data.close()
        #this creates a new csv file with modified data
        for card in self.all_cards:
            #data = open('cards_list.csv', mode = 'a', newline='')
            csv_writer = csv.writer(data, delimiter = ',')
            csv_writer.writerow([card.row, card.front, card.back, card.days, card.rank])
            #data.close()
        data.close()
  
    # this method represents a full day's cycle
    def cycle(self):
        # we create the new deck with cards that have days == 1
        review_deck = self.create_review_deck()
        # we review it
        self.review(review_deck)

    # this method returns the difficult cards, where miss > 2
    def get_hard_cards(self):
        hard_cards = [card for card in self.all_cards if card.miss > 2]
        return hard_cards
