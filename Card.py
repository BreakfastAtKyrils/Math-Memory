class Card:

   

    # the front and the back of the card are self-explanatory
    # the rank is the rank of the card is the stack pile, the higher the rank, t    he better memorized it is
    # the days attribute decrements every day, and when days = 0, the card is to    be reviewed today
    # id is to quickly find the card row in the .csv file
    def __init__(self, front, back, row, rank=1, days=1, miss=0):
        self.front = front
        self.back = back
        self.rank = rank
        self.row = row
        self.days = days
        self.miss = miss


    #toString method
    def toString(self):
        return 'ID: ' + str(self.row) + '    Card Front: ' + str(self.front) + '    Card Back: ' + str(self.back) + '    Rank: ' + str(self.rank) + '    Days until next review: ' + str(self.days) + '    Misses: ' + str(self.miss)

    # getter & setter methods
    def getFront(self):
        return self.front

    def getBack(self):
        return self.back

    def getRank(self):
        return self.rank
    
    def getRow(self):
        return self.row

    def getDays(self):
        return self.days

    def setFront(newFront):
        self.front = newFront

    def setBack(newBack):
        self.back = newBack

    def setRank(newRank):
        self.rank = newRank

    def setDays(newDays):
        self.days = newDays

    def check(self, answer):
        if self.back == str(answer):
            print('Correct!')
            return True
        else:
            print('Wrong!')
            return False

    #this method substracts 1 from the days attribute, to be called every day at midnight. The if statement makes sure we don't get a negative amount of days
    def newDay(self):
        if self.days == 0:
            self.days = 0
        else:
            olddays = self.days
            self.days = olddays - 1

    #this method is called once a Card has been answered, to move it up or down the stacks, and to reset the amount of days until the next review
    def answered(self, result):
        oldrank = self.rank
        if result == True:
            # the upper limit is 7, meaning with 100% retention you will still get the question once a week
            if oldrank == 7:
                self.rank = oldrank
            #if the answer is correct, we move the card up a rank
            elif oldrank < 7:
                self.rank = oldrank + 1
        elif result == False:
            # as soon as a card is answered wrong, it goes back into the first rank
            self.rank = 1
            # we also add 1 to the miss counter, to keep track of recurring mistakes
            oldmiss = self.miss
            self.miss = oldmiss + 1

        #once the rank is set, we reset the days attribute to the amount of days before the next review (equal to the card rank)
        self.days = self.rank


