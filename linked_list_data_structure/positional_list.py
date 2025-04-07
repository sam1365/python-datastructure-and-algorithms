from linked_list_data_structure.doubly_linked_list import BaseDoubleLinkedList

class PositionalList(BaseDoubleLinkedList):
    """Positional List Data Structure"""

    class Position:
        """An abstraction representing the position of an element in a positional list."""

        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            """Return the element at the current position."""

            return self._node.data

        def __eq__(self, other):
            """Return true if other is a Position  representing the same location."""

            return type(self) is type(other) and self._node == other._node

        def __ne__(self, other):
            """Return true if other does not represent the same location."""

            return not (self == other)

    def _validate_position(self, position):
        """Returns position's node or raise error."""

        if not isinstance(position, self.Position):
            raise TypeError('position must be of type Position')

        if position._container is not self:
            raise ValueError('position does not belong to this container')

        if position._node.next is None:
            raise ValueError('position is no longer valid')

        return position._node

    def _make_position(self, node):
        """Returns postion of the  given node or None if it's a sentinel."""

        if node is self._sentinel_tail or node is self._sentinel_head:
            return None
        else:
            return self.Position(self, node)

    def first(self):
        """Returns the first position in the positional list."""

        return self._make_position(self._sentinel_head.next)

    def last(self):
        """Returns the last position in the positional list."""

        return self._make_position(self._sentinel_tail.next)

    def before(self, position):
        """Returns position before given position."""

        node = self._validate_position(position)
        return self._make_position(node.prev)

    def after(self, position):
        """Returns position after given position."""

        node = self._validate_position(position)
        return self._make_position(node.next)

    def _insert_between(self, e, predecessor, successor):
        """
        Add element between existing nodes and return new Position.
        """

        node = super()._insert_between_nodes(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        return self._insert_between(e, self._sentinel_head, self._sentinel_head.next)

    def __iter__(self):
        """Iterates over the positional list."""

        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)
