Found 1 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
F
======================================================================
FAIL: test_books_page_shows_books (catalog.tests.BooksPageTests.test_books_page_shows_books)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Coolk\Documents\CIDM3312\book-catalog\catalog\tests.py", line 16, in test_books_page_shows_books
    self.assertContains(response, "Test Book")
    ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: False is not true : Couldn't find 'Test Book' in the following response
b'<html>\n<head>\n    <title>Catalog</title>\n</head>\n<body>\n    <nav>\n    <a href="/">Books</a> |\n    <a href="/publishers/">Publishers</a> |\n    <a href="/reviews/">Reviews</a>\n</nav>\n\n    \n<h1>Books</h1>\n    <ul>\n    \n    </ul>\n\n</body>\n</html>'

----------------------------------------------------------------------
Ran 1 test in 0.021s

FAILED (failures=1)
Destroying test database for alias 'default'...


This message tells me that my test's second assertion was false. In other words, that my test couldn't find the test book that I told my test to find on the "Books" page.




Question 1. Your models use two foreign keys. Pick one of them. Name which model carries the ForeignKey and which model it points at, and explain why you arranged it that way. What would be different about the data you entered if you had reversed it?

Q1 Answer: My Book model has a foreign key "publisher", which points to one publisher. I arranged it this way because each book should only have one publisher, while each publisher can have more than one book. If I reversed it, that would mean each publisher would have a foreign key pointing to only one book. In that instance, each publisher could have only one book, while each book could have several publishers.

Question 2. You added one field of your own to Book. Which field type did you choose, and why that type rather than another? What would you lose if you had stored the same fact as a CharField?

Q2 Answer: I added a DateField to my Book model. This stores a date in a specific format. That specific format is why DateField is different to a CharField. DateField stores data in the format of YYYY-MM-DD. Additionally, on my Books page, the date stored is automatically converted to a English format when displayed. If I used CharField, it would have just displayed the date as numbers.