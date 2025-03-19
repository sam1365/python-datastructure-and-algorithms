from tree_data_structure.abstract_tree import AbstractTree

class AbstractBinaryTree(AbstractTree):
    """
    Represents an abstract class for binary tree, which is a type of AbstractTree.

    Inherits from:
        AbstractTree: The base abstract class for tree data structure.

    Methods:
        right(self, p):  Returns the position of p's right child.
        left(self, p):  Returns the position of p's left child.
        sibling(self, p):  Returns the position of p's sibling.
        child(self, p):  Returns the position of p's children.
    """

    def right(self, p):
        """Return position of p's right child."""

        raise NotImplementedError('right is not implemented')

    def left(self, p):
        """Return position of p's left child."""

        raise NotImplementedError('left is not implemented')

    def sibling(self, p):
        """Return position of p's sibling."""

        parent = self.parent(p)
        if parent is None:
            return None
        if self.right(parent) == p:
            return self.left(p)
        if self.left(parent) == p:
            return self.right(p)

    def children(self, p):
        """Return position of p's children."""

        if self.right(p) is not None:
            yield self.right(p)
        if self.left(p) is not None:
            yield self.left(p)
