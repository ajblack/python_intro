import random
shuffledCards=[]
tableau_one=[]
tableau_two=[]
tableau_two=[]
tableau_three=[]
tableau_four=[]
tableau_five=[]
tableau_six=[]
tableau_seven=[]
burn_pile=[]

class Card(object):
 def __init__(self,suit,rank,id):
  self.suit=suit
  self.rank=rank
  self.id=id

 def get_card_info(self):
  if self.rank > 1 and self.rank < 11:
    print self.rank, "of ",self.suit
  elif self.rank == 1:
    print "ace of ",self.suit
  elif self.rank == 11:
    print "jack of ", self.suit
  elif self.rank == 12:
    print "queen of ", self.suit
  elif self.rank == 13:
    print "king of ",self.suit


 
class The_Deck(object):
  def __init__(self,list_of_cards):
    self.list_of_cards=list_of_cards
  def shuffleDeck(self):
    for i in range(52):
      random_card_num = random.randint(0,len(self.list_of_cards)-1)
      card_to_be_inserted=self.list_of_cards.pop(random_card_num)    
      shuffledCards.append(card_to_be_inserted)



class The_Game(object):
  def __init__(self,deck):
    self.deck=deck
    self.deck.shuffleDeck()

  def recite_game_status(self):
    print "here is the status of your game..."
    first_c=tableau_one.pop(0)
    print "your first tableau has ", len(tableau_one), " cards in it and there is a ",
    first_c.get_card_info(), 
    print"on top"
    tableau_one.insert(0,first_c)

    second_c=tableau_two.pop(0)
    print "your second tableau has ", len(tableau_two), " cards in it and there is a ",
    second_c.get_card_info(), 
    print"on top"
    tableau_two.insert(0,second_c)

    third_c=tableau_three.pop(0)
    print "your third tableau has ", len(tableau_three), " cards in it and there is a ",
    third_c.get_card_info(), 
    print"on top"
    tableau_one.insert(0,first_c)

    fourth_c=tableau_four.pop(0)
    print "your fourth tableau has ", len(tableau_four), " cards in it and there is a ",
    fourth_c.get_card_info(), 
    print"on top"
    tableau_four.insert(0,fourth_c)

    fifth_c=tableau_five.pop(0)
    print "your fifth tableau has ", len(tableau_five), " cards in it and there is a ",
    fifth_c.get_card_info(), 
    print "on top"
    tableau_one.insert(0,fifth_c)

    sixth_c=tableau_six.pop(0)
    print "you sixth tableau has ", len(tableau_six), " cards in it and there is a ",
    sixth_c.get_card_info(), 
    print "on top"
    tableau_one.insert(0,sixth_c)

    seventh_c=tableau_seven.pop(0)
    print "you seventh tableau has ", len(tableau_seven), " cards in it and there is a ",
    seventh_c.get_card_info(), 
    print" on top"
    tableau_seven.insert(0,seventh_c)

  def deal_initial_tableaus(self):
    tableau_one.insert(0,self.deal_single_card())
    tableau_two.insert(0,self.deal_single_card())
    tableau_three.insert(0,self.deal_single_card())
    tableau_four.insert(0,self.deal_single_card())
    tableau_five.insert(0,self.deal_single_card())
    tableau_six.insert(0,self.deal_single_card())
    tableau_seven.insert(0,self.deal_single_card())

    

    tableau_two.insert(0,self.deal_single_card())
    tableau_three.insert(0,self.deal_single_card())
    tableau_four.insert(0,self.deal_single_card())
    tableau_five.insert(0,self.deal_single_card())
    tableau_six.insert(0,self.deal_single_card())
    tableau_seven.insert(0,self.deal_single_card())

    tableau_three.insert(0,self.deal_single_card())
    tableau_four.insert(0,self.deal_single_card())
    tableau_five.insert(0,self.deal_single_card())
    tableau_six.insert(0,self.deal_single_card())
    tableau_seven.insert(0,self.deal_single_card())

    tableau_four.insert(0,self.deal_single_card())
    tableau_five.insert(0,self.deal_single_card())
    tableau_six.insert(0,self.deal_single_card())
    tableau_seven.insert(0,self.deal_single_card())

    tableau_five.insert(0,self.deal_single_card())
    tableau_six.insert(0,self.deal_single_card())
    tableau_seven.insert(0,self.deal_single_card())

    tableau_six.insert(0,self.deal_single_card())
    tableau_seven.insert(0,self.deal_single_card())

    tableau_seven.insert(0,self.deal_single_card())

    
#should deal a single card from the "end" of the shuffled deck
  def deal_single_card(self):
    return shuffledCards.pop(0)

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

  game=The_Game(theDeckInitial)
  game.deal_initial_tableaus()
  game.recite_game_status()
  


if __name__ == "__main__":
  main()












