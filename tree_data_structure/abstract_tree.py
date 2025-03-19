class TreeAbstractPosition:
    """Abstract class that represents position of an element in a tree.

    Methods:
        element(self): Returns the element at this position.
        __eq__(self, other): Returns True if this position is equal to the other.
        __nq__(self, other): Returns True if this position is not equal to the other.
    """

    def element(self):
        """Return the element at this position."""

        raise NotImplementedError('Element is not implemented yet')

    def __eq__(self, other):
        """Return True if this position is equal to the other."""

        raise NotImplementedError('Equality is not implemented yet')

    def __ne__(self, other):
        """Return True if this position is not equal to the other."""

        return not (self == other)

class AbstractTree:
    """Abstract base class that represents a tree data structure.

    Methods:
        __len__(self): Returns the length of the tree.
        is_empty(self): Returns True if the tree is empty.
        root(self): Returns the position of root of the tree.
        is_root(self, p): Returns True if p is root of the tree.
        parent(self, p): Returns the position of p's parent in the tree.
        children(self, p): Returns the children of p in the tree.
        number_of_children(self, p): Returns the number of children of p in the tree.
        is_leaf(self, p): Returns True if p is leaf.
        depth(self, p): Returns the depth of p in the tree.
        length(self, p): Returns the length of p in the tree.
    """

    def __len__(self):
        """Return the length of the tree."""

        raise NotImplementedError('len is not implemented yet')

    def is_empty(self):
        """Return True if the tree is empty."""

        return len(self) == 0

    def root(self):
        """Return the position of root of the tree."""

        raise NotImplementedError('root is is not implemented yet')
    def is_root(self, p):
        """Return True if p is root of the tree.

        Args:
            p (Position): Position of p in the tree.
        """

        return self.root() == p

    def parent(self, p):
        """Return the position of p's parent in the tree.

        Args:
            p (Position): Position of p in the tree.
        """

        raise NotImplementedError('parent is is not implemented yet')

    def children(self, p):
        """Return the children of p in the tree.

        Args:
            p (Position): Position of p in the tree.
        """

        raise NotImplementedError('children is not implemented yet')

    def number_of_children(self, p):
        """Return the number of children of p in the tree.

        Args:
            p (Position): Position of p in the tree.
        """

        raise NotImplementedError('number_of_children is not implemented yet')
    
    def is_leaf(self, p):
        """Return True if p is a leaf of the tree.

        Args:
            p (Position): Position of p in the tree.
        """

        return self.number_of_children(p) == 0

    def depth(self, p):
        """Return the depth of p in the tree.

        Args:
            p (Position): Position of p in the tree.
        """

        if self.is_root(p):
            return 0
        return 1 + self.depth(self.parent(p))

    def height(self, p):
        """Return the height of p in the tree.

        Args:
            p (Position): Position of p in the tree.
        """

        if self.is_leaf(p):
            return 0
        return 1 + max(self.depth(child) for child in self.children(p))