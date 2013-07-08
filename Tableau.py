


class Tableau(object):
    def __init__(self):
        self.isEmpty = False
        self.tableau_stack = []

    def add_card(self, the_card):
        self.tableau_stack.insert(0, the_card)

    def get_length(self):
        return len(self.tableau_stack)

    def isnt_empty(self):
        if len(self.tableau_stack) > 0:
            return True
        else:
            return False

    def get_card_at(self, index):
        return self.tableau_stack[index]

    def insert(self,the_card,the_space):
        self.tableau_stack.insert(the_space,the_card)









