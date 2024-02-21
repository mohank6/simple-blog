from app.author.accessor import AuthorAccessor
from app.post import post as post_business


class Author:

    @staticmethod
    def get_all_authors():
        authors = AuthorAccessor.get_all_authors()
        if not authors:
            raise ValueError
        return authors

    @staticmethod
    def get_author_by_id(id):
        author = AuthorAccessor.get_author_by_id(id)
        if not author:
            raise ValueError
        return author

    @staticmethod
    def delete_author(id):
        post_business.Post.delete_posts_by_author(id)
        AuthorAccessor.delete_author(id)
