from tree_data_structure.abstract_tree import TreeAbstractPosition
from tree_data_structure.abstract_binary_tree import AbstractBinaryTree
from queue_data_structure.linked_queue import LinkedQueue


class BinaryTreeNode:
    """
    Node class for storing a node in a binary tree.

    Attributes:
        _element: element of the  node.
        _parent: parent of the  node.
        _left: left child of the  node.
        _right: right child of the  node.

    Methods:
        __init__: initializes the node and sets the attributes.
    """

    def __init__(self, element, parent=None, left=None, right=None):
        """
        Initializes the node with the given element.
        Also sets the parent and left and right attributes if exists.
        """

        self._element = element
        self._parent = parent
        self._left = left
        self._right = right


class BinaryTreePosition(TreeAbstractPosition):
    """
    Position class for Representing location of an element in a binary tree.

    Attributes:
        _node: node of the element.
        _container: container of the element.
    """

    def __init__(self, container,  node):
        """Initializes the Position class."""

        self._container = container
        self._node = node

    def element(self):
        """Returns the element of the position."""

        return self._node._element

    def __eq__(self, other):
        """Returns true if other is a position that represents same location."""

        return type(other) is type(self) and other._node is self._node


class LinkedBinaryTree(AbstractBinaryTree):
    """Linked Binary Tree Data Structure.

    Inherits from:
        AbstractBinaryTree: The base abstract class for binary tree data structure.

    Attributes:
        _root: root of the binary tree.
        _size: size of the binary tree.

    Methods:
        __init__: initializes the binary tree and sets the attributes.
        __len__: returns the length of the binary tree.
        _validate_position: validates given position.
        _make_position: Makes an instance of BinaryTreePosition.
        root: returns the root of the binary tree.
        parent: returns the parent of the given position.
        left: returns the left child of the given position.
        right: returns the right child of the given position.
        number_of_children: returns the number of children of the given position.
        add_root: adds an element as the root of the binary tree.
        add_left: adds an element as the left child of a position.
        add_right: adds an element as the right child of a position.
        replace: replaces the element of a node with another element.
        delete: delete an element from the binary tree.
        attach: attach two binary trees to a position as its children.
    """

    def __init__(self):
        """Initializes the LinkedBinaryTree class.
        Also sets the attributes.

        """

        self._root = None
        self._size = 0

    def __len__(self):
        """Returns the length of the binary tree."""

        return self._size

    def _validate_position(self, position):
        """Checks if the given position is valid and returns its node.

        Args:
            position: an instance of BinaryTreePosition.
        """

        if not isinstance(position, BinaryTreePosition):
            raise TypeError("Position must be of type BinaryTreePosition")
        if position._container != self:
            raise ValueError("Position does not belong to this container")
        if position._node._parent == position._node:
            raise ValueError("Position does not belong to this node")
        if position._node._parent == position._node:
            raise ValueError("Position is not valid")
        return position._node

    def _make_position(self, node):
        """Makes an instance of BinaryTreePosition and returns it.

        Args:
            node: an instance of BinaryTreeNode.
        """

        if node is None:
            return None
        return BinaryTreePosition(self, node)

    def root(self):
        """Returns the root of the binary tree."""

        return self._make_position(self._root)

    def parent(self, position):
        """Returns the parent of the given position.

        Args:
            position: an instance of BinaryTreePosition.
        """

        node = self._validate_position(position)
        return self._make_position(node._parent)

    def left(self, position):
        """Returns the left child of the given position.

        Args:
            position: an instance of BinaryTreePosition.
        """

        node = self._validate_position(position)
        return self._make_position(node._left)

    def right(self, position):
        """Returns the right child of the given position."""

        node = self._validate_position(position)
        return self._make_position(node._right)

    def number_of_children(self, position):
        """Returns the number of children of the position.

        Args:
            position: an instance of BinaryTreePosition;
            Which this method calculates its number of children.
        """

        count = 0
        node = self._validate_position(position)
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count

    def add_root(self, e):
        """Adds an element as the root of the binary tree."""
        if self._root is not None:
            raise ValueError("Root already exists")
        self._size = 1
        self._root = BinaryTreeNode(e)
        return self._make_position(self._root)

    def add_left(self, position, e):
        """Add an element as the left child of given position.

        Args:
            position: an instance of BinaryTreePosition as parent.
            e: an element to create an instance of BinaryTreeNode
            as left child of position.
        """

        node = self._validate_position(position)
        if node._left is not None:
            raise ValueError("Left child already exists")

        node._left = BinaryTreeNode(e)
        self._size += 1
        return self._make_position(node._left)

    def add_right(self, position, e):
        """Add an element as the right child of given position.

        Args:
            position: an instance of BinaryTreePosition as parent.
            e: an element to create an instance of BinaryTreeNode
            as right child of position.
        """

        node = self._validate_position(position)
        if node._right is not None:
            raise ValueError("Right child already exists")

        node._right = BinaryTreeNode(e)
        self._size += 1
        return self._make_position(node._right)

    def replace(self, position, e):
        """Replaces the element of the position with the given element.

        Args:
            position: an instance of BinaryTreePosition as parent.
            e: an element to replace with element of the given position.
        """

        node = self._validate_position(position)
        old_node = node._element
        node._element = e
        return old_node

    def delete(self, position):
        """Deletes a node from the binary tree.

        Args:
            position: an instance of BinaryTreePosition
            where the node belongs to it.
        """

        node = self._validate_position(position)

        if self.number_of_children(position) == 2:
            raise ValueError("Position has two children")

        child = node._left if node._left is not None else node._right
        if child is not None:
            child._parent = node._parent

        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if parent._left is not None:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1

        # node deprecation
        node._parent = node
        return node._element

    def attach(self, position, tree1, tree2):
        """Attaches two binary trees to the given position.

        Args:
            position: an instance of BinaryTreePosition as parent for attachment
            of two binary trees.
            tree1: the first binary tree as left child of position.
            tree2: the second binary tree as right child of position.
        """

        node = self._validate_position(position)

        if not self.is_leaf(position):
            raise ValueError("Position must be leaf")

        if not type(self) is type(tree1) is type(tree2):
            raise TypeError("Trees must have same type")

        self._size += len(tree1) + len(tree2)

        if not tree1.is_empty():
            node._left = tree1._root
            tree1._root = None
            tree1._size = 0

        if not tree2.is_empty():
            node._right = tree2._root
            tree2._root = None
            tree1._size = 0

    def preorder(self):
        """Preorder traversal of the binary tree."""

        if not self.is_empty():
            for p in self._preorder_subtree(self.root()):
                yield p

    def _preorder_subtree(self, p):
        """Preorder traversal of subtree routed at position p."""

        yield p
        for child in p.children(p):
            for result in self._preorder_subtree(child):
                yield result

    def postorder(self):
        """Postorder traversal of the binary tree."""

        if not self.is_empty():
            for p in self._postorder_subtree(self.root()):
                yield p

    def _postorder_subtree(self, p):
        """Postorder traversal of subtree routed at position p."""

        for child in p.children(p):
            for result in self._postorder_subtree(child):
                yield result
        yield p

    def breadthfirst(self):
        """Breadth-first traversal of the binary tree."""

        if not self.is_empty():
            linked_queue = LinkedQueue()
            linked_queue.enqueue(self.root())
            while not linked_queue.is_empty():
                p = linked_queue.dequeue()
                yield p
                for child in p.children(p):
                    linked_queue.enqueue(child)
