import pytest

from linked_list_data_structure.positional_list import PositionalList

class TestPositionalList:
    """
    Testing PositionalList Class
    """

    @pytest.fixture(autouse=True)
    def setup(self):
        """Initialize an instance of PositionalList Class for testing purpose."""

        self.positional_list = PositionalList()

    def test_add_first(self):
        """
        Test add_first method of PositionalList.
        """

        assert len(self.positional_list) == 0
        self.positional_list.add_first(31)
        assert len(self.positional_list) == 1
        self.positional_list.first().element() == 31

    def test_add_last(self):
        """
        Test add_last method of PositionalList.
        """

        assert len(self.positional_list) == 0
        self.positional_list.add_first(31)
        self.positional_list.add_last(37)
        assert len(self.positional_list) == 2
        self.positional_list.last().element() == 37

    def test_before(self):
        """
        Test before method of PositionalList.
        """

        assert len(self.positional_list) == 0
        self.positional_list.add_first(31)
        self.positional_list.add_last(37)
        assert len(self.positional_list) == 2
        last = self.positional_list.last()
        assert self.positional_list.before(last).element() == 31

    def test_after(self):
        """
        Test after method of PositionalList.
        """

        assert len(self.positional_list) == 0
        self.positional_list.add_first(31)
        self.positional_list.add_last(37)
        assert len(self.positional_list) == 2
        first = self.positional_list.first()
        assert self.positional_list.after(first).element() == 37


    def test_add_before(self):
        """
        Test add_before method of PositionalList.
        """

        assert len(self.positional_list) == 0
        self.positional_list.add_first(31)
        self.positional_list.add_before(self.positional_list.first(), 37)
        assert len(self.positional_list) == 2
        first = self.positional_list.first()
        assert self.positional_list.after(first).element() == 31

    def test_add_after(self):
        """
        Test add_after method of PositionalList.
        """

        assert len(self.positional_list) == 0
        self.positional_list.add_first(31)
        self.positional_list.add_after(self.positional_list.first(), 37)
        assert len(self.positional_list) == 2
        first = self.positional_list.first()
        assert self.positional_list.after(first).element() == 37
