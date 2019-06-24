#import Node

class tree(object):
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root != None

    def size(self):
        return self._size(self.root)

    def _size(self, node):
        if not node:
            return 0
        return 1 + self._size(node.get_left()) + self._size(node.get_right())

    def height(self):
        return self._height(self.root)
    
    def _height(self, node):
        if not node:
            return 0
        return 1 + max(self.height_(node.get_left), self.height_(node.get_right))
    
    def find(self, query):
        query = Node(query)
        return self._find(self.root, query)
    
    def _find(self, node, query):
        if not node:
            return None
        if node == query:
            return node
        if node.get_right() and query < node:
            return self._find(node.get_right, query)
	
        elif node.get_right() and node < query:
            return self._find(node.get_right(), query)

        else:
            return None

    def insert(self, val):
        val = Node(val)
        self._insert(self.root, val)

    def _insert(self, node, val):
        if not node:
            return val

        elif not node.get_left() and val < node:
            node.insert_left(val)
            return node

        elif not node.get_right() and node.get_datum() < val:
            node.insert_right(val)
            return node

        elif val < node.get_datum():
            self._insert(node.get_left(), val)

        elif node.get_datum() < val:
            self._insert(node.get_right, val)
        else:
            return None

	
        
