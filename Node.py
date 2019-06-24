#Binary Tree - Node Class

class Node(object):

    def __init__(self, datum):

        self.datum = datum
        self.left = None
        self.right = None

        return

    def insert_left(self, node):

        self.left = node

        return

    def insert_right(self, node):

        self.right = node

        return

    def __del__(self):
        self._delete_Node(self.left)
        self._delete_Node(self.right)

    def _delete_Node(self, node):
        if node and node.left:
            print("l")
            self._delete_Node(node.left)
        if node and node.right:
            print("r")
            self._delete_Node(node.right)
        if node and not node.right and not node.left:
            del node

    def get_datum(self):

        return(self.datum)

    def get_left(self):

        return(self.left)

    def get_right(self):

        return(self.rightx.get_L)

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



    
