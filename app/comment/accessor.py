from app.models import Comment
from typing import Optional, List


class CommentAccessor:
    @staticmethod
    def get_all_comments() -> Optional[List[Comment]]:
        comments = Comment.objects.filter(is_deleted=False).all()
        return comments

    @staticmethod
    def get_all_comments_of_post(post) -> Optional[List[Comment]]:
        comments = Comment.objects.filter(is_deleted=False, post=post).all()
        return comments

    @staticmethod
    def get_all_comments_by_email(email) -> Optional[List[Comment]]:
        comments = Comment.objects.filter(is_deleted=False, email=email).all()
        return comments

    @staticmethod
    def get_comment_by_id(id) -> Optional[Comment]:
        comment = Comment.objects.filter(is_deleted=False, id=id).first()
        return comment

    @staticmethod
    def delete_comment(id) -> None:
        comment = Comment.objects.filter(id=id).first()
        comment.is_deleted = True
        comment.save()

    @staticmethod
    def delete_all_comments_of_post(post) -> None:
        comments = Comment.objects.filter(post=post).all()
        for comment in comments:
            comment.is_deleted = True
            comment.save()
