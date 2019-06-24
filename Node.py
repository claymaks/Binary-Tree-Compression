#Binary Tree - Node Class

class Node(object):

    def __init__(self, datum):

        self.datum = datum
        self.left = None
        self.right = None

        return

    def ins_L(self, node):

        self.left = node

        return

    def ins_R(self, node):

        self.right = node

        return

    def del_L(self, node):

        self.left = None

        return

    def del_R(self, node):

        self.right = None

        return

    def get_D(self):

        return(self.datum)

    def get_L(self):

        return(self.left)

    def get_R(self):

        return(self.right)

    def __lt__(self, other):

        return(self.datum < other)

    def __gt__(self, other):

        return(self.datum > other)

    def __le__(self, other):

        return(self.datum <= other)

    def __ge__(self, other):

        return(self.datum >= other)

    def __eq__(self, other):

        return(self.datum == other)



    
