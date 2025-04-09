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
        assert len(self.positional_list) == 0
        self.positional_list.add_first(31)
        assert len(self.positional_list) == 1
        self.positional_list.first().element() == 31
        