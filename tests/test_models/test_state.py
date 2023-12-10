import unittest
from models.base_model import BaseModel as BS
from models.state import State
from datetime import datetime

class TestState(unittest.TestCase):
    """A class to test the State class."""

    def test_state_is_subclass_of_base_model(self):
        # check that State inherits from BS
        self.assertTrue(issubclass(State, BS))

    def test_state_has_name_attribute(self):
        # check that State has name attribute
        state = State()
        self.assertTrue(hasattr(state, "name"))

    def test_state_name_is_string(self):
        # check that State name is string
        state = State()
        state.name = "California"
        self.assertIsInstance(state.name, str)

    def test_isntance(self):
        # check that Review attributes have the correct types
        state = State()
        self.assertIsInstance(State, BS)
        self.assertIsInstance(state.id, str)
        self.assertIsInstance(state.created_at, datetime)
        self.assertIsInstance(state.updated_at, datetime)
        self.assertIsInstance(state.name, str)


if __name__ == '__main__':
    unittest.main()
