from app.post.accessor import PostAccessor
from app.author import author as author_business
from app.category import category as category_business


class Post:
    @staticmethod
    def get_all_posts():
        posts = PostAccessor.get_all_posts()
        if not posts:
            raise ValueError
        return posts

    @staticmethod
    def get_post_by_id(id):
        post = PostAccessor.get_post_by_id(id)
        if not post:
            raise ValueError
        return post

    @staticmethod
    def get_posts_by_author(id):
        try:
            author = author_business.Author.get_author_by_id(id)
        except ValueError as e:
            raise e
        posts = PostAccessor.get_all_posts_of_author(author)
        if not posts:
            raise ValueError
        return posts

    @staticmethod
    def get_posts_of_category(id):
        try:
            category = category_business.Category.get_category_by_id(id)
        except ValueError as e:
            raise e
        posts = PostAccessor.get_posts_of_category(category)
        if not posts:
            raise ValueError
        return posts

    @staticmethod
    def delete_posts_by_author(id):
        try:
            author = author_business.Author.get_author_by_id(id)
        except ValueError as e:
            raise e
        PostAccessor.delete_posts_by_author(author)

    @staticmethod
    def delete_post(id):
        post = PostAccessor.get_post_by_id(id)
        if not post:
            raise ValueError
        PostAccessor.delete_post(id)
