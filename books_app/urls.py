from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('add_book', views.add_book),
    path('show_book/<int:id>', views.show_book),
    path('add_author_to_book/<int:id>', views.add_author_to_book)
]
