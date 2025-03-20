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
