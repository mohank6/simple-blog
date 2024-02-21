from django.urls import path, include
from app.author import view as author_view
from app.category import view as categories_view

urlpatterns = [
    path('v1/authors/', author_view.get_all_authors, name='get_all_authors'),
    path('v1/authors/<str:id>', author_view.get_author_by_id, name='get_author_by_id'),
    path('v1/authors/create/', author_view.create_author, name='create_author'),
    path('v1/authors/update/<str:id>', author_view.update_author, name='update_author'),
    path('v1/authors/delete/<str:id>', author_view.delete_author, name='delete_author'),
    path(
        'v1/categories/', categories_view.get_all_categories, name='get_all_categories'
    ),
    path(
        'v1/categories/<str:id>',
        categories_view.get_category_by_id,
        name='get_category_by_id',
    ),
    path(
        'v1/categories/name/<str:name>',
        categories_view.get_category_by_name,
        name='get_category_by_name',
    ),
    path(
        'v1/categories/create/', categories_view.create_category, name='create_category'
    ),
    path(
        'v1/categories/update/<str:id>',
        categories_view.update_category,
        name='update_category',
    ),
    path(
        'v1/categories/delete/<str:id>',
        categories_view.delete_category,
        name='delete_category',
    ),
]
