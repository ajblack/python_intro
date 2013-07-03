import random
from Card import Card
from Tableau import Tableau
from Deck import The_Deck

shuffledCards=[]

class The_Game(object):
  def __init__(self,deck):
    self.deck=deck
    self.deck.shuffleDeck()
    self.tableau_one = Tableau()
    self.tableau_two = Tableau()
    self.tableau_three = Tableau()
    self.tableau_four = Tableau()
    self.tableau_five = Tableau()
    self.tableau_six = Tableau()
    self.tableau_seven = Tableau()

  def shuffle_deck(self,init_deck):
    for i in range(52):
      random_card_num = random.randint(0,len(self.list_of_cards)-1)
      card_to_be_inserted=self.init_deck.pop(random_card_num)    
      shuffledCards.append(card_to_be_inserted)


  def recite_game_status(self):
    print "here is the status of your game..."
    if self.tableau_one.isnt_empty():
      first_c = self.tableau_one.get_card_at(0) 
      print "your first tableau has ", self.tableau_one.get_length(), " cards in it and the top card is a ",
      first_c.get_card_info()
    else:
      print "tableau one is empty"

    if self.tableau_two.isnt_empty():
      second_c = self.tableau_two.get_card_at(0)
      print "your second tableau has ", self.tableau_two.get_length(), " cards in it and the top card is a ",
      second_c.get_card_info()
    else:
      print "tableau two is empty"

    if self.tableau_three.isnt_empty():
      third_c = self.tableau_three.get_card_at(0)
      print "your third tableau has ", self.tableau_three.get_length(), " cards in it and the top card is a ",
      third_c.get_card_info()
    else:
      print "tableau three is empty"
      

    if self.tableau_four.isnt_empty():
      fourth_c = self.tableau_four.get_card_at(0)
      print "your fourth tableau has ", self.tableau_four.get_length(), " cards in it and the top card is a ",
      fourth_c.get_card_info()
    else:
      print "tableau four is empty"

    if self.tableau_five.isnt_empty():
      fifth_c = self.tableau_five.get_card_at(0)
      print "your fifth tableau has ", self_tableau_five.get_length(), " cards in it and the top card is a ",
      fifth_c.get_card_info()
    else:
      print "tableau five is empty"

    if self.tableau_six.isnt_empty():
      sixth_c = self.tableau_six.get_card_at(0)
      print "you sixth tableau has ", self.tableau_six.get_length(), " cards in it and the top card is a ",
      sixth_c.get_card_info()
    else:
      print "tableau six is empty"

    if self.tableau_seven.isnt_empty():
      seventh_c = self.tableau_seven.get_card_at(0)
      print "you seventh tableau has ", self.tableau_seven.get_length(), " cards in it and the top card is a ",
      seventh_c.get_card_info()
    else:
      print "tableau seven is empty"

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
    if(len(shuffledCards)>0):
      return shuffledCards.pop(0)
    else:
      return "the deck of shuffled cards is empty"