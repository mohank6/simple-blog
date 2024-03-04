from django.urls import path, include
from app.author import view as author_view
from app.author import auth
from app.category import view as categories_view
from app.post import view as post_view
from app.comment import view as comment_view

urlpatterns = [
    path('v1/signup/', auth.signup, name='signup'),
    path('v1/login/', auth.login, name='login'),
    path('v1/verify/', auth.verify_email, name='verify_email'),
    path('v1/forgot-password/', auth.forgot_password, name='forgot_password'),
    path('v1/reset-password/', auth.reset_password, name='reset_password'),
    path('v1/change-password/', auth.change_password, name='change_password'),
    path('v1/authors/', author_view.get_all_authors, name='get_all_authors'),
    path('v1/authors/<str:id>', author_view.get_author_by_id, name='get_author_by_id'),
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
    path('v1/posts/', post_view.get_all_posts, name='get_all_posts'),
    path('v1/posts/<str:id>', post_view.get_post_by_id, name='get_post_by_id'),
    path('v1/posts/create/', post_view.create_post, name='create_post'),
    path('v1/posts/update/<str:id>', post_view.update_post, name='update_post'),
    path(
        'v1/posts/author/<str:id>',
        post_view.get_posts_by_author,
        name='get_posts_by_author',
    ),
    path(
        'v1/posts/category/<str:id>',
        post_view.get_posts_of_category,
        name='get_posts_of_category',
    ),
    path('v1/posts/delete/<str:id>', post_view.delete_post, name='delete_post'),
    path('v1/comments/', comment_view.get_all_comments, name='get_all_comments'),
    path(
        'v1/comments/<str:id>', comment_view.get_comment_by_id, name='get_comment_by_id'
    ),
    path(
        'v1/comments/post/<str:id>',
        comment_view.get_all_comments_of_post,
        name='get_all_comments_of_post',
    ),
    path('v1/comments/create/', comment_view.create_comment, name='create_comment'),
    path(
        'v1/comments/update/<str:id>',
        comment_view.update_comment,
        name='update_comment',
    ),
    path(
        'v1/comments/delete/<str:id>',
        comment_view.delete_comment,
        name='delete_comment',
    ),
]
