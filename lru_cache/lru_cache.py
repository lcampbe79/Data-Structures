import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import (DoublyLinkedList, ListNode)

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        #limits how many node it can hold 10
        self.limit = limit
        #current number of nodes it's holding
        self.size = 0
        #dictionary for access (hash table) s well as a storage dict that provides fast access
        #to every node stored in the cache.
        self.storage = {}
        #variable used to set the value being set by Doublylinked list
        #a doubly-linked list that holds the key-value entries in the correct order
        self.order = DoublyLinkedList()
        

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        #if key is in storage
        if key in self.storage:
            #move to end
            node = self.storage[key]
            #update order
            self.order.move_to_end(node)
            #return value
            return node.value[1] #<-tuple
        #if not:
        else:
            #return None
            return None

        # #if there is not a key
        # if not self.hash_table.get(key):
        #     return None
        # else:
        #     #new node created with a key
        #     node = self.hash_table.get(key)
        #     #moves to front since it's most recently used
        #     self.Linked_List.move_to_front(node)
        #     #
        #     return node.value

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        #check to see if key is in the dict
        if key in self.storage:
            #if it is
            node = self.storage[key] #<-grab the full node in the dict
            #overwrite the value
            node.value = (key, value) #<- creates tuple
            #move to the end
            self.order.move_to_end(node)#<-adding something new
            #exit function nothing left to do
            return

            #check if cache is full
        if self.size == self.limit:
            #if cache is full:
            #remove oldest from cache from the dict 
            del self.storage[self.order.head.value[0]]# <-check 55 minutes
            #remove oldest from cache from the DLL
            self.order.remove_from_head()
            #reduce the size
            self.size -=1

        #add to the linked list (KVP) tuple
        self.order.add_to_tail((key, value))
        #add key and value to dictionary
        self.storage[key] = self.order.tail
        #increment the size
        self.size += 1



        # #checks if node exists
        # node = self.hash_table.get(key)
        # #checks if node is none then moves to front as MRU
        # if node is not None:
        #     node.value = value
        #     self.Linked_List.move_to_front(node)
        # else: #if the node doesn't exist and at limit
        #     if self.size == self.limit:
        #         #remove from end
        #         self.Linked_List.remove_from_tail()
        #         #decreases the number of nodes
        #         self.size -= 1
            
        #     #adds to the hash table
        #     new_node = ListNode(value)
        #     self.hash_table[key] = new_node
            
        #     #add to front
        #     self.Linked_List.add_to_head(new_node)

        #     #adds to number of nodes it's holding
        #     self.size += 1

    
