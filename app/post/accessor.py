from app.models import Post
from typing import List, Optional


class PostAccessor:

    @staticmethod
    def get_all_posts() -> Optional[List[Post]]:
        posts = Post.objects.filter(is_deleted=False).all()
        return posts

    @staticmethod
    def get_post_by_id(id: str) -> Optional[Post]:
        post = Post.objects.filter(id=id, is_deleted=False).first()
        return post

    @staticmethod
    def get_all_posts_of_author(author) -> Optional[List[Post]]:
        posts = Post.objects.filter(author=author, is_deleted=False).all()
        return posts

    @staticmethod
    def get_posts_of_category(category) -> Optional[List[Post]]:
        posts = Post.objects.filter(categories=category, is_deleted=False).all()
        return posts

    @staticmethod
    def delete_post(id: str) -> None:
        post = Post.objects.filter(id=id).first()
        post.is_deleted = True
        post.save()

    @staticmethod
    def delete_posts_by_author(author) -> None:
        posts = Post.objects.filter(author=author)
        for post in posts:
            post.is_deleted = True
            post.save()
