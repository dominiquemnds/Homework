"""CS330 Spring 2019: Quiz 2 (take home)."""

import unittest
import shelf
import book

# Steps to consider when writing any unit test:
# 1) Create an instance of the object whose behavior you want to test.
# 2) Ensure that the instance is initialized appropriately to exhibit the behavior need to meet the test objective.
# 3) Use the TestCase methods (self.assertXXXXX()) to show the test objective is met.
# 4) Verify object state before and after (where needed) to show that test actions affect the object's state.
# 5) Run your test class the same way you'd run any Python program.

# PyUnit Docs: https://docs.python.org/3/library/unittest.html


class TestShelf(unittest.TestCase):
    """Tests Shelf behavior."""

    def setUp(self):
        """Use or delete this method."""
        self.little_women = book.Book("Little Women", ("Louisa", "May", "Alcott"))
        self.little_women.SetPages(204)
        self.little_women.SetCoverType(book.CoverType.HARDCOVER)
        
        self.hobbit = book.Book("The Hobbit", ("J", "R R", "Tolkien"))
        self.hobbit.SetPages(689)
        self.hobbit.SetCoverType(book.CoverType.HARDCOVER)
        
        self.war_and_peace = book.Book("War and Peace", ("Leo", "", "Tolstoy"))
        self.war_and_peace.SetPages(584)
        self.war_and_peace.SetCoverType(book.CoverType.SOFTCOVER)
        
        self.assertIsInstance(book.Book("Little Women", ("Louisa", "May", "Alcott")), book.Book)
        #using assert just to check that the syntax for the set up is correct
        self.shelf0 =shelf.Shelf();

        pass

    # Write unit tests for these Shelf class methods and behaviors:

    def test_AddBook(self):
        """Tests that a book is successfully added to a shelf."""
        before=self.shelf0.GetBookCount()
        self.shelf0.AddBook(self.little_women)
        after=self.shelf0.GetBookCount()

        self.assertTrue(before < after)
        pass

    def test_RemoveBook(self):
        """Tests that a book is successfully removed from a shelf."""
        self.shelf0.AddBook(self.little_women)
        before=self.shelf0.GetBookCount()
        self.shelf0.RemoveBook(self.little_women.GetTitleFormatted())
        after=self.shelf0.GetBookCount()
        self.assertTrue(before > after)
        pass

    def test_AddBook_reduces_shelf_capacity(self):
        """Tests that shelf capacity is reduced after adding a book."""
        before=self.shelf0.GetAvailableCapacity()
        self.shelf0.AddBook(self.war_and_peace)
        after=self.shelf0.GetAvailableCapacity()
        self.assertTrue(before > after)
        pass

    def test_RemoveBook_increases_shelf_capacity(self):
        """Tests that shelf capacity is increased after removing a book."""
        self.shelf0.AddBook(self.war_and_peace)
        before=self.shelf0.GetAvailableCapacity()
        self.shelf0.RemoveBook(self.war_and_peace.GetTitleFormatted())
        after=self.shelf0.GetAvailableCapacity()
        self.assertTrue(before < after)
        pass

    # Extra Credit
    def test_shelf_space_exhausted(self):
        """Tests that an exception is raised when adding a book to a shelf with insufficient space."""
        

        pass
if __name__ == '__main__':
    unittest.main()
