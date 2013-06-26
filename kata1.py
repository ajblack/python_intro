import random
shuffledCards=[]

class Card(object):
 def __init__(self,suit,rank,id):
  self.suit=suit
  self.rank=rank
  self.id=id

class The_Deck(object):
  def __init__(self,list_of_cards):
    self.list_of_cards=list_of_cards
  def shuffleDeck(self):
    for card in self.list_of_cards:
      random_card_num = random.randint(0,len(self.list_of_cards)-1)
      print random_card_num

      card_to_be_inserted=self.list_of_cards.pop(random_card_num)
      
      shuffledCards.append(card_to_be_inserted)





#need a method to shuffle the deck into a list or array or something like that
#need a data type to hold the deck
#need data types to hold the 7 tableu piles
#need data types to hold the played cards
#need data types to hold the discard pile


def main():
  ace_of_spades=Card("Spades",1,1)
  ace_of_diamonds=Card("Diamonds",1,2)
  ace_of_hearts=Card("Hearts",1,3)
  ace_of_clubs=Card("Clubs",1,4)

  two_of_spades=Card("Spades",2,5)
  two_of_diamonds=Card("Diamonds",2,6)
  two_of_hearts=Card("Hearts",2,7)
  two_of_clubs=Card("Clubs",2,8)

  three_of_spades=Card("Spades",3,9)
  three_of_diamonds=Card("Diamonds",3,10)
  three_of_hearts=Card("Hearts",3,11)
  three_of_clubs=Card("Clubs",3,12)

  four_of_spades=Card("Spades",4,13)
  four_of_diamonds=Card("Diamonds",4,14)
  four_of_hearts=Card("Hearts",4,15)
  four_of_clubs=Card("Clubs",4,16)

  five_of_spades=Card("Spades",5,17)
  five_of_diamonds=Card("Diamonds",5,18)
  five_of_hearts=Card("Hearts",5,19)
  five_of_clubs=Card("Clubs",5,20)

  six_of_spades=Card("Spades",6,21)
  six_of_diamonds=Card("Diamonds",6,22)
  six_of_hearts=Card("Hearts",6,23)
  six_of_clubs=Card("Clubs",6,24)

  seven_of_spades=Card("Spades",7,25)
  seven_of_diamonds=Card("Diamonds",7,26)
  seven_of_hearts=Card("Hearts",7,27)
  seven_of_clubs=Card("Clubs",7,28)

  eight_of_spades=Card("Spades",8,29)
  eight_of_diamonds=Card("Diamonds",8,30)
  eight_of_hearts=Card("Hearts",8,31)
  eight_of_clubs=Card("Clubs",8,32)

  nine_of_spades=Card("Spades",9,33)
  nine_of_diamonds=Card("Diamonds",9,34)
  nine_of_hearts=Card("Hearts",9,35)
  nine_of_clubs=Card("Clubs",9,36)

  ten_of_spades=Card("Spades",10,37)
  ten_of_diamonds=Card("Diamonds",10,38)
  ten_of_hearts=Card("Hearts",10,39)
  ten_of_clubs=Card("Clubs",10,40)

  jack_of_spades=Card("Spades",11,41)
  jack_of_diamonds=Card("Diamonds",11,42)
  jack_of_hearts=Card("Hearts",11,43)
  jack_of_clubs=Card("Clubs",11,44)

  queen_of_spades=Card("Spades",12,45)
  queen_of_diamonds=Card("Diamonds",12,46)
  queen_of_hearts=Card("Hearts",12,47)
  queen_of_clubs=Card("Clubs",12,48)

  king_of_spades=Card("Spades",13,49)
  king_of_diamonds=Card("Diamonds",13,50)
  king_of_hearts=Card("Hearts",13,51)
  king_of_clubs=Card("Clubs",13,52)

  theDeckInitial=The_Deck([ace_of_clubs,ace_of_hearts,ace_of_diamonds,ace_of_spades,
     two_of_clubs,two_of_hearts,two_of_diamonds,two_of_spades,
     three_of_clubs,three_of_hearts,three_of_diamonds,three_of_spades,
     four_of_clubs,four_of_hearts,four_of_diamonds,four_of_spades,
     five_of_clubs,five_of_hearts,five_of_diamonds,five_of_spades,
     six_of_clubs,six_of_hearts,six_of_diamonds,six_of_spades,
     seven_of_clubs,seven_of_hearts,seven_of_diamonds,seven_of_spades,
     eight_of_clubs,eight_of_hearts,eight_of_diamonds,eight_of_spades,
     nine_of_clubs,nine_of_hearts,nine_of_diamonds,nine_of_spades,
     ten_of_clubs,ten_of_hearts,ten_of_diamonds,ten_of_spades,
     jack_of_clubs,jack_of_hearts,jack_of_diamonds,jack_of_spades,
     queen_of_clubs,queen_of_hearts,queen_of_spades,queen_of_diamonds,
     king_of_clubs,king_of_hearts,king_of_diamonds,king_of_spades])


  for card in theDeckInitial.list_of_cards:
    print "current suit :", card.suit, card.id

  print "now to test the shuffling"
  theDeckInitial.shuffleDeck()

  for card in shuffledCards:
    print "current suit :", card.suit, card.id






if __name__ == "__main__":
  main()












