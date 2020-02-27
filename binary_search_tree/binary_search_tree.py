import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        #value < self.value look left
        if value < self.value:
            #if something is there already
            if self.left:
                #recurse left
                self.left.insert(value)
            #if not
            else:
                #insert left
                self.left = BinarySearchTree(value)
        #value < self.value look right
        if value >= self.value:
            #if something is there already
            if self.right:
                #recurse right
                self.right.insert(value)
            #if not
            else:
                #insert right
                self.right = BinarySearchTree(value)
                

        # #looks to see if there is a value
        # if value < self.value:
        #     if self.left == None:
        #         #becomes the new value
        #         self.left = BinarySearchTree(value)
        #     else: 
        #         #if there is a value then inserts it
        #         self.left.insert(value)
        # elif value >= self.value:
        #     if self.right == None:
        #         #becomes the new value
        #         self.right = BinarySearchTree(value)
        #     else: 
        #         #if there is a value then inserts it
        #         self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    ##SEARCH
    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        if target >= self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        if not self.right:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    ##TRAVERSAL DFT
    def for_each(self, cb):
        #call CB on self.value
        cb(self.value)
            #if left 
        if self.left:
            #call for_each
            self.left.for_each(cb)
        #if right
        if self.right:
            #call for_each
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        #if 
        # Check left, if left is None, that's the smallest number
        if self.left is not None:
            self.left.in_order_print(node)
        # Check right
        if self.right is not None:
            self.right.in_order_print(node)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        #initialize stack
        queue = Queue()
        #push root to stack
        queue.enqueue(node)
        #while loop to check stack not empty
        while queue.len != 0:
            #pop top item out of stack & into temp variable
            temp: BinarySearchTree = queue.denqueue()
            if temp:
                # if temp var has right put that into the stack
                if temp.right:
                    queue.enqueue(temp.right)
                #if temp var has left, put that into the stack
                if temp.left:
                    queue.enqueue(temp.left)
                print(temp.value)
            #Do something (print, return)
            else:
                break
        

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        #initialize stack
        stack = Stack()
        #push root to stack
        stack.push(node)
        #while loop to check stack not empty
        while stack.len != 0:
            #pop top item out of stack & into temp variable
            temp: BinarySearchTree = stack.pop()
            if temp:
                # if temp var has right put that into the stack
                if temp.right:
                    stack.push(temp.right)
                #if temp var has left, put that into the stack
                if temp.left:
                    stack.push(temp.left)
                print(temp.value)
            #Do something (print, return)
            else:
                break
        
        

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
