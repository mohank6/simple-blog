from .accessor import CommentAccessor
from app.post import post as post_business


class Comment:

    @staticmethod
    def get_all_comments():
        comments = CommentAccessor.get_all_comments()
        if not comments:
            raise ValueError
        return comments

    @staticmethod
    def get_comment_by_id(id):
        comment = CommentAccessor.get_comment_by_id(id)
        if not comment:
            raise ValueError
        return comment

    @staticmethod
    def get_all_comments_of_post(id):
        try:
            post = post_business.Post.get_post_by_id(id)
        except ValueError as e:
            raise e
        comments = CommentAccessor.get_all_comments_of_post(post)
        if not comments:
            raise ValueError
        return comments

    @staticmethod
    def delete_comment(id):
        comment = CommentAccessor.get_comment_by_id(id)
        if not comment:
            raise ValueError
        CommentAccessor.delete_comment(id)

    @staticmethod
    def delete_all_comments_of_post(post):
        CommentAccessor.delete_all_comments_of_post(post)
