from typing import Any


class TreeNode:
    def __init__(self, key: int, value: Any, right: 'TreeNode' = None,
                 left: 'TreeNode' = None, parent: 'TreeNode' = None):
        self.key = key
        self.value = value
        self.right = right
        self.left = left
        self.parent = parent

    def __repr__(self) -> str:
        return f"TreeNode({self.key}, {self.value})"

    @property
    def depth(self) -> int:
        """Return depth of the node, i.e. the number of parents/grandparents etc."""
        depth = 0
        current_node = self.parent
        while current_node:
            depth += 1
            current_node = current_node.parent
        return depth

    @property
    def is_external(self) -> bool:
        """Return if node is an external node (= leaf)."""
        return self.left is None and self.right is None

    @property
    def is_internal(self) -> bool:
        """Return if node is an internal node."""
        return self.left is not None or self.right is not None
