import random

from Card import Card
from Deck import Deck
from Tableau import Tableau

shuffled_cards = []


class Game(object):
    def __init__(self, deck):
        self.deck = deck
        self.shuffle_deck #why does it say that this statement is useless?  I hope not
        self.tableau_one = Tableau()
        self.tableau_two = Tableau()
        self.tableau_three = Tableau()
        self.tableau_four = Tableau()
        self.tableau_five = Tableau()
        self.tableau_six = Tableau()
        self.tableau_seven = Tableau()
        self.dest_one = Tableau()
        self.dest_two = Tableau()
        self.dest_three = Tableau()
        self.dest_four = Tableau()
        self.burn_pile = Tableau()
        self.is_won = False
        self.is_lost = False


    def shuffle_deck(self, init_deck):
        for i in range(52):
            random_card_num = random.randint(0, len(init_deck) - 1)
            card_to_be_inserted = init_deck.pop(random_card_num)
            shuffled_cards.append(card_to_be_inserted)

    def check_if_game_complete(self):
        if self.dest_one.get_length() + self.dest_two.get_length() + self.dest_three.get_length() + self.dest_four.get_length() == 52:
            self.is_won = True
            return True
        #####still need to figure out a way if the game is lost (if there is nothing left to do but an endless loop)
        else:
            return False

    def make_move(self):
        return

    def recite_game_status(self):
        print "here is the status of your game..."

        if self.burn_pile.isnt_empty():
            print "the shown cards in the burn pile are ",
            self.burn_pile.show_face_up_cards()

        if self.tableau_one.isnt_empty():
            self.tableau_one.get_card_at(0).face_up = True
            print "your first tableau has ", self.tableau_one.get_length(), " cards in it and the top card is a ",
            self.tableau_one.get_card_at(0).get_card_info()

        else:
            print "tableau one is empty"


        if self.tableau_two.isnt_empty():
            self.tableau_two.get_card_at(0).face_up = True
            print "your second tableau has ", self.tableau_two.get_length(), " cards in it and the top card is a ",
            self.tableau_two.get_card_at(0).get_card_info()
        else:
            print "tableau two is empty"

        if self.tableau_three.isnt_empty():
            self.tableau_three.get_card_at(0).face_up = True
            print "your third tableau has ", self.tableau_three.get_length(), " cards in it and the top card is a ",
            self.tableau_two.get_card_at(0).get_card_info()
        else:
            print "tableau three is empty"

        if self.tableau_four.isnt_empty():
            self.tableau_four.get_card_at(0).face_up = True
            print "your fourth tableau has ", self.tableau_four.get_length(), " cards in it and the top card is a ",
            self.tableau_four.get_card_at(0).get_card_info()
        else:
            print "tableau four is empty"

        if self.tableau_five.isnt_empty():
            self.tableau_five.get_card_at(0).face_up = True
            print "your fifth tableau has ", self.tableau_five.get_length(), " cards in it and the top card is a ",
            self.tableau_five.get_card_at(0).get_card_info()
        else:
            print "tableau five is empty"

        if self.tableau_six.isnt_empty():
            self.tableau_six.get_card_at(0).face_up = True
            print "you sixth tableau has ", self.tableau_six.get_length(), " cards in it and the top card is a ",
            self.tableau_six.get_card_at(0).get_card_info()
        else:
            print "tableau six is empty"

        if self.tableau_seven.isnt_empty():
            self.tableau_seven.get_card_at(0).face_up = True
            print "you seventh tableau has ", self.tableau_seven.get_length(), " cards in it and the top card is a ",
            self.tableau_seven.get_card_at(0).get_card_info()
        else:
            print "tableau seven is empty"

            #reciting initial status's of the destination tableaus...which is of course empty
        if self.dest_one.isnt_empty():
            self.dest_one.get_card_at(0).face_up = True
            print "you first destination tableau has ", self.dest_one.get_length(), " cards in it and the top card is a ",
            self.dest_one.get_card_at(0).get_card_info()
        else:
            print "destination tableau one is empty"

        if self.dest_two.isnt_empty():
            self.dest_two.get_card_at(0).face_up = True
            print "you second destination tableau has ", self.dest_two.get_length(), " cards in it and the top card is a ",
            self.dest_two.get_card_at(0).get_card_info()
        else:
            print "destination tableau two is empty"

        if self.dest_three.isnt_empty():
            self.dest_three.get_card_at(0).face_up = True
            print "you third destination tableau has ", self.dest_three.get_length(), " cards in it and the top card is a ",
            self.dest_three.get_card_at(0).get_card_info()
        else:
            print "destination tableau three is empty"

        if self.dest_four.isnt_empty():
            self.dest_four.get_card_at(0).face_up = True
            print "you fourth destination tableau has ", self.dest_four.get_length(), " cards in it and the top card is a ",
            self.dest_four.get_card_at(0).get_card_info()
        else:
            print "destination tableau four is empty"


def deal_initial_tableaus(self):
    self.burn_pile.insert(0, self.deal_single_card())
    self.burn_pile.get_card_at(0).face_up = True
    self.tableau_one.insert(0, self.deal_single_card())
    self.tableau_two.insert(0, self.deal_single_card())
    self.tableau_three.insert(0, self.deal_single_card())
    self.tableau_four.insert(0, self.deal_single_card())
    self.tableau_five.insert(0, self.deal_single_card())
    self.tableau_six.insert(0, self.deal_single_card())
    self.tableau_seven.insert(0, self.deal_single_card())

    self.tableau_two.insert(0, self.deal_single_card())
    self.tableau_three.insert(0, self.deal_single_card())
    self.tableau_four.insert(0, self.deal_single_card())
    self.tableau_five.insert(0, self.deal_single_card())
    self.tableau_six.insert(0, self.deal_single_card())
    self.tableau_seven.insert(0, self.deal_single_card())

    self.tableau_three.insert(0, self.deal_single_card())
    self.tableau_four.insert(0, self.deal_single_card())
    self.tableau_five.insert(0, self.deal_single_card())
    self.tableau_six.insert(0, self.deal_single_card())
    self.tableau_seven.insert(0, self.deal_single_card())

    self.tableau_four.insert(0, self.deal_single_card())
    self.tableau_five.insert(0, self.deal_single_card())
    self.tableau_six.insert(0, self.deal_single_card())
    self.tableau_seven.insert(0, self.deal_single_card())

    self.tableau_five.insert(0, self.deal_single_card())
    self.tableau_six.insert(0, self.deal_single_card())
    self.tableau_seven.insert(0, self.deal_single_card())

    self.tableau_six.insert(0, self.deal_single_card())
    self.tableau_seven.insert(0, self.deal_single_card())

    self.tableau_seven.insert(0, self.deal_single_card())

    self.tableau_one.get_card_at(0).face_up = True
    self.tableau_one.get_card_at(0).face_up = True
    self.tableau_one.get_card_at(0).face_up = True
    self.tableau_one.get_card_at(0).face_up = True
    self.tableau_one.get_card_at(0).face_up = True
    self.tableau_one.get_card_at(0).face_up = True
    self.tableau_one.get_card_at(0).face_up = True


def deal_single_card(self):
    if (len(shuffled_cards) > 0):
        return shuffled_cards.pop(0)
    else:
        return "the deck of shuffled cards is empty"