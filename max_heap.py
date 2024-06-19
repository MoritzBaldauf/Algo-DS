
class MaxHeap:
    def __init__(self, input_array):
        """
        @param input_array from which the heap should be created
        @raises ValueError if list is None.
        Creates a bottom-up max heap in place.
        """
        self.heap = None
        self.size = 0

        if input_array is None: # error handling for no inputs
            raise ValueError("No input array found")

        self.heap = input_array
        self.size = len(input_array)

        self.construct_max_heap()

    def get_heap(self):
        # helper function for testing, do not change
        return self.heap

    def get_size(self):
        """
        @return size of the max heap
        """
        return self.size

    def contains(self, val):
        """
        @param val to check if it is contained in the max heap
        @return True if val is contained in the heap else False
        @raises ValueError if val is None.
        Tests if an item (val) is contained in the heap. Does not search the entire array sequentially, but uses the
        properties of a heap.
        """
        if val is None:
            raise ValueError("No Value provided")

        next_node = [0]
        while next_node:
            current = next_node.pop(0)
            if current < self.size:
                if self.heap[current] == val:
                    return True
                if self.heap[current] >= val:
                    left = 2*current + 1
                    right = 2 * current + 2
                    if left < self.size:
                        next_node.append(left)
                    if right < self.size:
                        next_node.append(right)
        return False


    def sort(self):
        """
        This method sorts (ascending) the list in-place using HeapSort, e.g. [1,3,5,7,8,9]
        """
        end = self.size -1

        while end > 0:
            self.swap(0, end)
            end -= 1

            self.shift_down(0 ,end)

    def is_empty(self) -> bool:
        """
        Reused from A5
        @return True if the min heap is empty, False otherwise
        """
        return self.size == 0

    def remove_max(self):
        """
        Removes and returns the maximum element of the heap
        @return maximum element of the heap or None if heap is empty
        """
        # Note code adapted from A5 min_heap
        if self.is_empty():
            return None

        max_val = self.heap[0] # save the biggest value for return
        self.swap(0, self.size - 1) # move root element to the end of the list -> allows easy deletion
        self.heap.pop() # rm last element of list
        self.size -= 1
        if self.size > 0:
            self.shift_down(0, self.size-1)
        return max_val

    def construct_max_heap(self):
        """
        Converts the array into a max heap using the bottom-up construction approach.
        """
        start_point = (self.size //2) -1 # find first non leaf node

        for i in range(start_point, -1, -1): # go to the root node
            self.shift_down(i, self.size-1)

    def shift_down(self, index: int, end=None):
        """
        Sifts down the node at index start to the proper place such that all nodes below
        the start index are in heap order.
        """
        # adapted code from min_heap

        while self.left_child(index) <= end: # Nodes without children
            largest = self.left_child(index) # assume smallest value is in left child -> save index

            if self.right_child(index) <= end and self.heap[self.right_child(index)] > self.heap[largest]: # check right child > left child
                largest = self.right_child(index)
            if self.heap[largest] <= self.heap[index]: # We swap if current node < child
                break
            self.swap(index, largest)
            index = largest

    # NOTE: These functions are the same as in A5 min_heap
    def parent(self, index: int) -> int:
        return (index - 1) // 2

    def left_child(self, index: int) -> int:
        return 2 * index + 1

    def right_child(self, index: int) -> int:
        return 2 * index + 2

    def swap(self, index1: int, index2: int):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1] #swap node 1 with node 2