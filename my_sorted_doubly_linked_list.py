from my_list_node import MyListNode


class MySortedDoublyLinkedList:
    """A base class providing a doubly linked list representation."""

    def __init__(self, head: 'MyListNode' = None, tail: 'MyListNode' = None, size: int = 0) -> None:
        """Create a list and default values are None."""
        self._head = head
        self._tail = tail
        self._size = size

    def __len__(self) -> int:
        """Return the number of elements in the list."""
        return self._size

    def __str__(self) -> str:
        """Return linked list in string representation."""
        result = []
        node = self._head
        while node:
            result.append(node.elem)
            node = node.next_node
        return str(result)

    # The following methods have to be implemented.

    def get_value(self, index: int) -> int:
        """Return the value (elem) at position 'index' without removing the node.

        Args:
            index (int): 0 <= index < length of list

        Returns:
            (int): Retrieved value.

        Raises:
            ValueError: If the passed index is not an int or out of range.
        """
        if not isinstance(index, int) or index < 0 or index >= len(self):
            raise ValueError
        else:
            cur_node = self._head
            for i in range(index): # Go through the linked list until we reach the index value
                cur_node = cur_node.next_node
        return cur_node.elem


    def search_value(self, val: int) -> int:
        """Return the index of the first occurrence of 'val' in the list.

        Args:
            val (int): Value to be searched.

        Returns:
            (int): Retrieved index.

        Raises:
            ValueError: If val is not an int.
        """
        if not isinstance(val, int):
            raise ValueError("Value must be an integer")
        #cur_node = self._head
        for i in range(self.__len__()): # go through the entire list
            if self.get_value(i) == val:
                return i

        return -1

    def insert(self, val: int) -> None:
        """Add a new node containing 'val' to the list, keeping the list in ascending order.

        Args:
            val (int): Value to be added.

        Raises:
            ValueError: If val is not an int.
        """
        if not isinstance(val, int):
            raise ValueError("Value must be an integer")

        new_node = MyListNode(val)
        if self._head is None:
            self._head = new_node
            self._tail = new_node
        else:
            current = self._head
            while current is not None and current.elem <= val:
                prev = current
                current = current.next_node
            if current is None:
                prev.next_node = new_node # End insert
                new_node.prev_node = prev
                self._tail = new_node
            elif current == self._head:
                new_node.next_node = self._head # Start insert
                self._head.prev_node = new_node
                self._head = new_node
            else:
                prev.next_node = new_node # Middle insert
                new_node.prev_node = prev
                new_node.next_node = current
                current.prev_node = new_node
        self._size += 1

    def remove_first(self, val: int) -> bool:
        """Remove the first occurrence of the parameter 'val'.

        Args:
            val (int): Value to be removed.

        Returns:
            (bool): Whether an element was successfully removed or not.

        Raises:
            ValueError: If val is not an int.
        """
        if not isinstance(val, int):
            raise ValueError("Value must be an integer")

        current = self._head
        while current:
            if current.elem == val:
                if current == self._head:
                    self._head = current.next_node
                    if self._head:
                        self._head.prev_node = None
                elif current == self._tail:
                    self._tail = current.prev_node
                    self._tail.next_node = None
                else:
                    current.prev_node.next_node = current.next_node
                    current.next_node.prev_node = current.prev_node
                self._size -= 1
                return True
            current = current.next_node
        return False

    def remove_all(self, val: int) -> bool:
        """Remove all occurrences of the parameter 'val'.

        Args:
            val (int): Value to be removed.

        Returns:
            (bool): Whether elements were successfully removed or not.

        Raises:
            ValueError: If val is not an int.
        """
        if not isinstance(val, int):
            raise ValueError("Value must be an integer")

        removed = False
        current = self._head
        while current:
            next_node = current.next_node
            if current.elem == val:
                if current == self._head:
                    self._head = next_node
                    if self._head:
                        self._head.prev_node = None
                elif current == self._tail:
                    self._tail = current.prev_node
                    self._tail.next_node = None
                else:
                    current.prev_node.next_node = current.next_node
                    current.next_node.prev_node = current.prev_node
                self._size -= 1
                removed = True
            current = next_node
        return removed

    def remove_duplicates(self) -> None:
        """Remove all duplicate occurrences of values from the list."""
        if self._head is None:
            return

        current = self._head
        while current and current.next_node:
            if current.elem == current.next_node.elem:
                duplicate = current.next_node
                current.next_node = duplicate.next_node
                if duplicate.next_node:
                    duplicate.next_node.prev_node = current
                else:  # else if last note
                    self._tail = current
                self._size -= 1
            else:
                current = current.next_node

    def filter_n_max(self, n: int) -> None:
        """Filter the list to only contain the 'n' highest values.

        Args:
            n (int): 0 < n <= length of list

        Raises:
            ValueError: If the passed value n is not an int or out of range.
        """
        if not isinstance(n, int) or n <= 0 or n > self._size:
            raise ValueError("n must be an integer between 1 and the size of the list.")

        if n == self._size:
            return

        keep_count = n # calc num notes to keep

        current = self._tail
        for _ in range(keep_count - 1):
            current = current.prev_node

        self._head = current
        self._head.prev_node = None

        self._size = keep_count

    def filter_odd(self) -> None:
        """Filter the list to only contain odd values."""
        current = self._head
        while current:
            next_node = current.next_node
            if current.elem % 2 == 0:
                if current.prev_node: # delete node
                    current.prev_node.next_node = current.next_node
                if current.next_node:
                    current.next_node.prev_node = current.prev_node
                if current == self._head:  # current is head
                    self._head = current.next_node
                if current == self._tail:  # current is tail
                    self._tail = current.prev_node
                self._size -= 1
            current = next_node

    def filter_even(self) -> None:
        """Filter the list to only contain even values."""
        current = self._head
        while current:
            next_node = current.next_node
            if current.elem % 2 != 0:
                if current.prev_node: # delete node
                    current.prev_node.next_node = current.next_node
                if current.next_node:
                    current.next_node.prev_node = current.prev_node
                if current == self._head:  # current is head
                    self._head = current.next_node
                if current == self._tail:  # current is tail
                    self._tail = current.prev_node
                self._size -= 1
            current = next_node
