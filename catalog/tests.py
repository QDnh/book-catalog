from django.test import TestCase
from .models import Publisher, Book, Review
from django.urls import reverse

class BooksPageTests(TestCase):
    def test_books_page_shows_books(self):
        # Arrange 
        publisher = Publisher.objects.create(name="Test Publisher")
        book = Book.objects.create(publisher=publisher, title="Test Book", datepublished="2000-01-01")

        # Act
        response = self.client.get(reverse("books"))

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Book")