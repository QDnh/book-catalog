from django.shortcuts import render
from django.views.generic import ListView

from .models import Publisher, Book, Review

class BooksPageView(ListView):
    model = Book
    template_name = "books.html"
    context_object_name = "books"

class PublishersPageView(ListView):
    model = Publisher
    template_name = "publishers.html"
    context_object_name = "publishers"

class ReviewsPageView(ListView):
    model = Review
    template_name = "reviews.html"
    context_object_name = "reviews"