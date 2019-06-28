from Node import Node
import random

class tree(object):
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root == None

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
        return 1 + max(self._height(node.get_left()), self._height(node.get_right()))
    
    def find(self, query):
        #fix
        query = Node(query)
        return self._find(self.root, query)
    
    def _find(self, node, query):
        if not node:
            return None
        if node == query:
            return node
        if node.get_left() and query < node:
            return self._find(node.get_left(), query)
	
        elif node.get_right() and node < query:
            return self._find(node.get_right(), query)

        else:
            return None

    def insert(self, val):
        if self.is_empty():
            self.root = Node(val)
        else:
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
            self._insert(node.get_right(), val)
        else:
            return None

    def lcr_print(self):
        self._lcr_print(self.root)

    def _lcr_print(self, node):
        if node.get_left():
            self._lcr_print(node.get_left())
        print(node.get_datum(), end=" ")
        if node.get_right():
            self._lcr_print(node.get_right())


class huffman(object):
    def __init__(self):
        self.root = None
        self.log = []

    def is_empty(self):
        return self.root == None

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
        return 1 + max(self._height(node.get_left()), self._height(node.get_right()))
    
    def find_char(self, query):
        query = Node(query)
        if self.log == []:
            self._init_log(self.root, "")
            self.log = sorted(self.log, key=lambda x: x.get_datum()[1], reverse=True)
            
        for node in self.log:
            if node.get_datum()[0] == query.get_datum():
                return node.get_datum()[2]
        
        return "error"

    def _init_log(self, node, path):
        if node.get_datum()[0] == '':
            if node.get_left():
                self._init_log(node.get_left(), path + "0")
            if node.get_right():
                self._init_log(node.get_right(), path + "1")
        if not node.get_right() and not node.get_left():
            node.datum.append(path)
            self.log.append(node)

    def translate(self, bit):
        return self._translate(self.root, bit)

    def _translate(self, node, bit):
        if len(bit) > 0:
            if bit[0] == "0":
                if node.get_left():
                    return self._translate(node.get_left(), bit[1:])
                else:
                    return node.get_datum()[0], bit
            if bit[0] == "1":
                if node.get_right():
                    return self._translate(node.get_right(), bit[1:])
                else:
                    return node.get_datum()[0], bit
        return node.get_datum()[0], bit
            

    def insert(self, lst):
        if isinstance(lst[0], list):
            new_lst = []
            for i in lst:
                new_lst.append(Node(i))
            lst = new_lst
        if len(lst) > 1:
            #for i in lst:
                #print(i.get_datum(), end = " ")
            #print()
            temp = Node(['', lst[0].get_datum()[1] + lst[1].get_datum()[1]])
            temp.insert_left(lst[0])
            temp.insert_right(lst[1])
            lst.append(temp)
            lst = sorted(lst[2:], key=lambda x: x.get_datum()[1], reverse=False)
            self.insert(lst)
        else:
            self.root = lst[0]

    def lcr_print(self):
        self._lcr_print(self.root)
        print()

    def _lcr_print(self, node):
        if node.get_left():
            self._lcr_print(node.get_left())
        print(node.get_datum(), end=" ")
        if node.get_right():
            self._lcr_print(node.get_right())


    
        
        
if __name__ == "__main__":
    x = tree()
    x.insert(50)
    for i in range(0,100): 
        x.insert(random.randint(0,100))
    #x.lcr_print()

    h = huffman()
    h.insert([['a',1],['b',1],['c',1],['d',2],['e',6],['f',10],['g',15]])
    #h.lcr_print()
    #print()
    c = h.find_char('c')
    a = h.find_char('a')
    string = str(c + a)
    print(string)
    while string:
        char, string = h.translate(string)
        print(char, end = "")
    
    #print()
    #for i in h.log:
        #print(i.get_datum(), end = " ")
    

    
    
                 
