import unittest
from models.base_model import BaseModel as BS
from models.review import Review

class TestReview(unittest.TestCase):
    """A class to test the Review class."""

    def test_review_is_subclass_of_base_model(self):
        # check that Review inherits from BS
        self.assertTrue(issubclass(Review, BS))

    def test_review_has_attributes(self):
        # check that Review has the expected attributes
        review = Review()
        self.assertTrue(hasattr(review, "place_id"))
        self.assertTrue(hasattr(review, "user_id"))
        self.assertTrue(hasattr(review, "text"))

    def test_review_attributes_are_correct_types(self):
        # check that Review attributes have the correct types
        review = Review()
        review.place_id = "123"
        review.user_id = "456"
        review.text = "This place is awesome"
        self.assertIsInstance(review.place_id, str)
        self.assertIsInstance(review.user_id, str)
        self.assertIsInstance(review.text, str)

if __name__ == '__main__':
    unittest.main()
