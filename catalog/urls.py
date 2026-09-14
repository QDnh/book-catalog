from django.urls import path

from . import views

urlpatterns = [
    path("", views.BooksPageView.as_view(), name="books"),
    path("publishers/", views.PublishersPageView.as_view(), name="publishers"),
    path("reviews/", views.ReviewsPageView.as_view(), name="reviews"),
]
