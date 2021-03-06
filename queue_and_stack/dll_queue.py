import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Queue:
    def __init__(self):
        #keeps track of the size of the queue
        #but is redundant below should delete
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size +=1

    def dequeue(self):
        if self.size > 0:
            value = self.storage.remove_from_head()
            self.size -= 1
            return value
        else:
            return

    def len(self):
        return self.size
        #suggested to change to self.storage.__len__()