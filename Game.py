import random

class The_Game(object):
  def __init__(self,deck):
    self.deck=deck
    self.deck.shuffleDeck()
    self.first_tableau = Tableau()
    self.second_tableau = Tableau()
    self.third_tableau = Tableau()
    self.fourth_tableau = Tableau()
    self.fifth_tableau = Tableau()
    self.sixth_tableau = Tableau()
    self.seventh_tableau = Tableau()

  def set_initial_tableaus(self):
    self.first_tableau.tableau_stack = tableau_one
    self.second_tableau.tableau_stack = tableau_two
    self.third_tableau.tableau_stack = tableau_three
    self.fourth_tableau.tableau_stack = tableau_four
    self.fifth_tableau.tableau_stack = tableau_five
    self.sixth_tableau.tableau_stack = tableau_six
    self.seventh_tableau.tableau_stack = tableau_seven


  def recite_game_status(self):
    print "here is the status of your game..."
    if self.first_tableau.isEmpty== False:
      first_c=tableau_one[0]
      print "your first tableau has ", len(tableau_one), " cards in it and the top card is a ",
      first_c.get_card_info()
    else:
      print "tableau one is empty"

    if len(tableau_two)>0:
      second_c=tableau_two[0]
      print "your second tableau has ", len(tableau_two), " cards in it and the top card is a ",
      second_c.get_card_info()
    else:
      print "tableau two is empty"

    if len(tableau_three)>0:
      third_c=tableau_three[0]
      print "your third tableau has ", len(tableau_three), " cards in it and the top card is a ",
      third_c.get_card_info()
    else:
      print "tableau three is empty"
      

    if len(tableau_four)>0:
      fourth_c=tableau_four[0]
      print "your fourth tableau has ", len(tableau_four), " cards in it and the top card is a ",
      fourth_c.get_card_info()
    else:
      print "tableau four is empty"

    if len(tableau_five)>0:
      fifth_c=tableau_five[0]
      print "your fifth tableau has ", len(tableau_five), " cards in it and the top card is a ",
      fifth_c.get_card_info()
    else:
      print "tableau five is empty"

    if len(tableau_six)>0:
      sixth_c=tableau_six[0]
      print "you sixth tableau has ", len(tableau_six), " cards in it and the top card is a ",
      sixth_c.get_card_info()
    else:
      print "tableau six is empty"

    if len(tableau_seven)>0:
      seventh_c=tableau_seven[0]
      print "you seventh tableau has ", len(tableau_seven), " cards in it and the top card is a ",
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
    return shuffledCards.pop(0)