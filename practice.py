

class Node:
    def __init__(self, value=None):

        self.value = value
        self.left = None
        
    def __str__(self):
        return str(self.value)

    

    def insert(self, value):
        