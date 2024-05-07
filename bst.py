from typing import Any, Generator, Tuple

from tree_node import TreeNode


class BinarySearchTree:
    """Binary-Search-Tree implemented for didactic reasons."""

    def __init__(self, root: TreeNode = None):
        """Initialize BinarySearchTree.

        Args:
            root (TreeNode, optional): Root of the BST. Defaults to None.

        Raises:
            ValueError: root is neither a TreeNode nor None.
        """
        self._root = root
        self._size = 0 if root is None else 1
        self._num_of_comparisons = 0

    def insert(self, key: int, value: Any) -> None:
        """Insert a new node into BST.

        Args:
            key (int): Key which is used for placing the value into the tree.
            value (Any): Value to insert.

        Raises:
            ValueError: If key is not an integer.
            KeyError: If key is already present in the tree.
        """
        if key == None or value == None:
            raise ValueError

        new_node = TreeNode(key, value)
        if not self._root:
            self._root = new_node
            self._size = 1
        else:
            parent, node = None, self._root
            while node:
                parent = node
                if key < node.key:
                    node = node.left
                elif key > node.key:
                    node = node.right
                else:
                    raise KeyError(f"Key {key} already exists in the tree.")
            if key < parent.key:
                parent.left = new_node
            else:
                parent.right = new_node
            new_node.parent = parent
            self._size += 1


    def find(self, key: int) -> TreeNode:
        """Return node with given key.

        Args:
            key (int): Key of node.

        Raises:
            ValueError: If key is not an integer.
            KeyError: If key is not present in the tree.

        Returns:
            TreeNode: Node
        """
        if key == None:
            raise ValueError

        node = self._root
        while node:
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            else:
                return node
        raise KeyError(f"Key {key} not found in the tree.")

    @property
    def size(self) -> int:
        """Return number of nodes contained in the tree."""
        return self._size

    # If users instead call `len(tree)`, this makes it return the same as `tree.size`
    __len__ = size

    # This is what gets called when you call e.g. `tree[5]`
    def __getitem__(self, key: int) -> Any:
        """Return value of node with given key.

        Args:
            key (int): Key to look for.

        Raises:
            ValueError: If key is not an integer.
            KeyError: If key is not present in the tree.

        Returns:
            Any: [description]
        """
        return self.find(key).value

    def remove(self, key: int) -> None:
        """Remove node with given key, maintaining BST-properties.

        Args:
            key (int): Key of node which should be deleted.

        Raises:
            ValueError: If key is not an integer.
            KeyError: If key is not present in the tree.
        """
        if key == None:
            raise ValueError
        # Find the node to remove
        node = self._root
        parent = None
        while node and node.key != key:
            parent = node
            if key < node.key:
                node = node.left
            else:
                node = node.right

        if not node:  # The key is not found
            raise KeyError

        # Case 1: Node with two children
        if node.left and node.right:
            # Find the in-order successor (smallest in the right subtree)
            succ_parent = node
            successor = node.right
            while successor.left:
                succ_parent = successor
                successor = successor.left

            # Copy the successor's value to the node
            node.key = successor.key
            node.value = successor.value
            # Recursively remove the successor
            node = successor
            parent = succ_parent

        # Case 2: Node with only one child or no child
        child = node.left if node.left else node.right
        if not parent:
            # The node to remove is the root
            self._root = child
        elif parent.left == node:
            parent.left = child
        else:
            parent.right = child

        # If the child is not None, set its parent (only necessary if using parent pointers)
        if child:
            child.parent = parent

        self._size -= 1
        return True

    # Hint: The following 3 methods can be implemented recursively, and
    # the keyword `yield from` might be extremely useful here:
    # http://simeonvisser.com/posts/python-3-using-yield-from-in-generators-part-1.html

    # Also, we use a small syntactic sugar here:
    # https://www.pythoninformer.com/python-language/intermediate-python/short-circuit-evaluation/

    def inorder(self, node: TreeNode = None) -> Generator[TreeNode, None, None]:
        """Yield nodes in inorder."""
        node = node or self._root
        # This is needed in the case that there are no nodes.
        if not node:
            return iter(())
        yield from self._inorder(node)

    def preorder(self, node: TreeNode = None) -> Generator[TreeNode, None, None]:
        """Yield nodes in preorder."""
        node = node or self._root
        if not node:
            return iter(())
        yield from self._preorder(node)

    def postorder(self, node: TreeNode = None) -> Generator[TreeNode, None, None]:
        """Yield nodes in postorder."""
        node = node or self._root
        if not node:
            return iter(())
        yield from self._postorder(node)

    # this allows for e.g. `for node in tree`, or `list(tree)`.
    def __iter__(self) -> Generator[TreeNode, None, None]:
        yield from self._preorder(self._root)

    @property
    def is_valid(self) -> bool:
        """Return if the tree fulfills BST-criteria."""

        def is_valid_node(node, low=-float('inf'), high=float('inf')):
            if not node:
                return True
            if not (low < node.key < high):
                return False
            return (is_valid_node(node.left, low, node.key) and
                    is_valid_node(node.right, node.key, high))

        return is_valid_node(self._root)

    def return_max_key(self) -> TreeNode:
            """Return the node with the largest key (None if tree is empty)."""
            current = self._root
            while current and current.right:
                current = current.right
            return current

    def find_comparison(self, key: int) -> Tuple[int, int]:
        """Create an inbuilt python list of BST values in preorder and compute the number of comparisons needed for
           finding the key both in the list and in the BST.
           Return the numbers of comparisons for both, the list and the BST
        """
        #python_list = list(node.key for node in self._preorder())
        list_comparisons = 0
        bst_comparisons = 0
        python_list = list(node.key for node in self._preorder())
        # Count comparisons in list
        for item in python_list:
            list_comparisons += 1
            if item == key:
                break
        else:
            list_comparisons = float('inf')  # Key not found

        # Count comparisons in BST
        node = self._root
        while node:
            bst_comparisons += 1
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            else:
                break
        else:
            bst_comparisons = float('inf')  # Key not found

        return (list_comparisons, bst_comparisons)

    def __repr__(self) -> str:
        return f"BinarySearchTree({list(self._inorder(self._root))})"

    ####################################################
    # Helper Functions
    ####################################################

    def get_root(self):
        return self._root

    def _inorder(self, current_node):
        if current_node:
            yield from self._inorder(current_node.left)
            yield current_node
            yield from self._inorder(current_node.right)

    def _preorder(self, current_node):
        if current_node:
            yield current_node
            yield from self._preorder(current_node.left)
            yield from self._preorder(current_node.right)

    def _postorder(self, current_node):
        if current_node:
            yield from self._postorder(current_node.left)
            yield from self._postorder(current_node.right)
            yield current_node

    # You can of course add your own methods and/or functions!
    # (A method is within a class, a function outside of it.)


arr_list_1 = [5, 18, 1, 8, 14, 16, 13, 3]

"""def create_bst_from_list(list_):
    bst_solution = BinarySearchTree()
    for k in list_:
        bst_solution.insert(key=k, value=str(k))
    return bst_solution

bst_solution = create_bst_from_list(arr_list_1)
bst = BinarySearchTree(bst_solution.get_root())
bst._size = bst_solution.size

print(bst.find(18).depth)"""