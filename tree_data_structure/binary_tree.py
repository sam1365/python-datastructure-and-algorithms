from twisted.web import _element

from tree_data_structure.abstract_tree import TreeAbstractPosition
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
