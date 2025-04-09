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