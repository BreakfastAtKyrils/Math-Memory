import csv
class Deck:
    # all_cards will hold all the cards
    # cards_today is a temporary daily list holding only the cards scheduled for review
    # data is the .csv file from which the 2 previous lists are created

    def __init__(self):
        self.all_cards = []
        self.cards_today = []
        #set filename
        self.data = open('cards_list.csv', mode = 'w', newline='')

    #remove these
    def all_cards_toString(self):
        for x in range(0, len(self.all_cards)):
           return self.all_cards[x].toString()
        
    def all_cards_print(self):
        for x in range(0, len(self.all_cards)):
           print(self.all_cards[x].toString())
    
    def cards_today_toString(self):
        for x in range(0, len(self.cards_today)):
           return self.cards_today[x].toString()
        
    def cards_today_print(self):
        for x in range(0, len(self.cards_today)):
            index = self.cards_today[x]
            print(self.all_cards[index].toString())

    # this method takes the full deck, check whether days = 1,
    # if so, appends it to cards_today[]
    # adds a new card to the deck

    def today_deck(self):
        self.cards_today.clear()

    #for card in self.all_cards:
    #use "card"
        for x in range(0, len(self.all_cards)):
            if self.all_cards[x].days == 1:
                self.cards_today.append(x)
            else:
                pass

    def add_card(self, card):
        self.all_cards.append(card)
        self.make_csv()

    #this method reviews today's deck by asking user each question
    def review(self):
        #self.today_deck()
        for x in range(0, len(self.cards_today)):
            index = self.cards_today[x]
            question = self.all_cards[index].front
            answer = input('Question: ' + question)
            result = self.all_cards[index].check(answer)
            self.all_cards[index].answered(result)
        self.make_csv()

    #this is the method that decrements 1 every night at midnight from the days attribute
    def new_day(self):
        for x in range(0, len(self.all_cards)):
            if self.all_cards[x].days > 1:
                old_value =  self.all_cards[x].days
                self.all_cards[x].days = old_value - 1
            else:
                pass
        self.make_csv()

    #this method is called everytime there is a change to the Deck, it refreshes
    #the csv file to be up to date    
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
  
    #this method represents a full day's cycle
    def cycle(self):
        # we create the new deck with cards that have days == 1
        self.today_deck()
        # we review it
        self.review()

    #this method returns the difficult cards, where miss > 2
    def hard_cards(self):
        hard_cards = []
        for x in range(0, len(self.all_cards)):
            if self.all_cards[x].miss > 2:
                hard_cards.append(self.all_cards[x])
        return hard_cards

