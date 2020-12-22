class Node:
    global Lista
    Lista = []
    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

# Insert method to create nodes
    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
# findval method to compare the value with nodes
    def delete(self):
        global Lista
        x = Lista
        Lista = []

        while x != []:
            self.left = 0
            self.right = 0
            self.data = 0
            x=x[1:]
            
        self.left = None
        self.right = None
        #self.data = data

        
# Print the tree
    def PrintTree(self):
        global Lista
        if self.left:
            self.left.PrintTree()
        Lista.append(self.data),
        print( self.data),
        if self.right:
            self.right.PrintTree()
        return Lista
