import unittest
from models.base_model import BaseModel as BS
from models.state import State

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

if __name__ == '__main__':
    unittest.main()
