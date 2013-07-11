class Card(object):
    def __init__(self, suit, rank, id):
        self.suit = suit
        self.rank = rank
        self.id = id
        self.face_up = False

    def get_card_info(self):
        if self.rank > 1 and self.rank < 11:
            print self.rank, "of ", self.suit
        elif self.rank == 1:
            print "ace of ", self.suit
        elif self.rank == 11:
            print "jack of ", self.suit
        elif self.rank == 12:
            print "queen of ", self.suit
        elif self.rank == 13:
            print "king of ", self.suit


    def is_face_up(self):
        if self.face_up:
            return True
        else:
            return False
