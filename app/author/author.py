from app.author.accessor import AuthorAccessor
from app.post import post as post_business
from django.contrib.auth.hashers import check_password
from app.services import auth_service
from datetime import timedelta, datetime, timezone
from app.services import email_service


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

    @staticmethod
    def login(email, password):
        author = AuthorAccessor.get_author_by_email(email=email)
        if not author:
            raise ValueError
        is_valid = check_password(password=password, encoded=author.password)
        if not is_valid:
            raise ValueError
        token = auth_service.generate_token(author)
        return author, token

    @staticmethod
    def generate_and_send_otp(email):
        author = AuthorAccessor.get_author_by_email(email=email)
        email_service.generate_and_send_otp(author)

    @staticmethod
    def verify_otp(email, otp):
        author = AuthorAccessor.get_author_by_email(email=email)
        if not author:
            raise ValueError
        if author.is_verified:
            return None, {'verified': 'User is already verified'}
        is_valid = author.otp == otp and (
            datetime.now(timezone.utc) - author.otp_sent_at
        ) < timedelta(minutes=10)
        if not is_valid:
            raise ValueError
        author.otp = None
        author.is_verified = True
        author.save()
        token = auth_service.generate_token(author)
        return author, token
