from django.urls import path, include
from app.author import view as author_view

urlpatterns = [
    path('v1/authors/', author_view.get_all_authors, name='get_all_authors'),
    path('v1/authors/<str:id>', author_view.get_author_by_id, name='get_author_by_id'),
    path('v1/authors/create/', author_view.create_author, name='create_author'),
    path('v1/authors/update/<str:id>', author_view.update_author, name='update_author'),
    path('v1/authors/delete/<str:id>', author_view.delete_author, name='delete_author'),
]
