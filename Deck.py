import random
class The_Deck(object):
  def __init__(self,list_of_cards):
    self.list_of_cards=list_of_cards
  def shuffleDeck(self):
    for i in range(52):
      random_card_num = random.randint(0,len(self.list_of_cards)-1)
      card_to_be_inserted=self.list_of_cards.pop(random_card_num)    
      shuffledCards.append(card_to_be_inserted)
