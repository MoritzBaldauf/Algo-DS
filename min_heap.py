from typing import Optional


class MinHeap:
    def __init__(self):
        self.heap = []
        self.size = len(self.heap)

    def get_size(self) -> int:
        """
        @return number of elements in the min heap
        """
        return self.size

    def is_empty(self) -> bool:
        """
        @return True if the min heap is empty, False otherwise
        """
        return self.size == 0

    def insert(self, integer_val: int) -> None:
        """
        inserts integer_val into the min heap
        @param integer_val: the value to be inserted
        @raises ValueError if integer_val is None or not an int
        """
        if integer_val is None or not isinstance(integer_val, int):
            raise ValueError("No integer_val to be inserted")

        self.heap.append(integer_val) # Add element at the end of heap

        self.size += 1 # Update heap size
        self.up_heap(self.size - 1) # ensure heap property

    def get_min(self) -> Optional[int]:
        """
        returns the value of the minimum element of the PQ without removing it
        @return the minimum value of the PQ or None if no element exists
        """
        if self.is_empty():
            return None
        return self.heap[0] # smallest heap value (root) is at index 0

    def remove_min(self) -> Optional[int]:
        """
        removes the minimum element from the PQ and returns its value
        @return the value of the removed element or None if no element exists
        """
        if self.is_empty():
            return None
        min_val = self.heap[0] # save the smallest value for return
        self.swap(0, self.size - 1) # move root element to the end of the list -> allows easy deletion
        self.heap.pop() # rm last element of list
        self.size -= 1
        self.down_heap(0) # Maintain heap properties
        return min_val



## Helper functions
    def up_heap(self, index: int): # maintain heap properties -> parent node < child node
        while index > 0 and self.heap[index] < self.heap[self.parent(index)]: # check that the current node is not the root node AND the parent node needs to be bigger than the cild node
            self.swap(index, self.parent(index)) # Swap child node with parent node
            index = self.parent(index) # update index


    def down_heap(self, index: int): #maintiang heap property by moving a bigger element down in the heap
        while self.left_child(index) < self.size: # only process nodes that have children
            smallest = self.left_child(index) # assume smallest value is in left child -> save index
            if self.right_child(index) < self.size and self.heap[self.right_child(index)] < self.heap[smallest]: #chekc if right child is smaller than left child
                smallest = self.right_child(index) # if true update smallest index
            if self.heap[smallest] >= self.heap[index]: # check if current node is corretly placed
                break
            self.swap(index, smallest) # current node is smaller than child -> swap
            index = smallest


    def parent(self, index: int) -> int:
        return (index - 1) // 2

    def left_child(self, index: int) -> int:
        return 2 * index + 1

    def right_child(self, index: int) -> int:
        return 2 * index + 2

    def swap(self, index1: int, index2: int):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1] #swap node 1 with node 2

