from django.forms import ValidationError
from app.author.accessor import AuthorAccessor
from app.post import post as post_business
from django.contrib.auth.hashers import check_password
from app.services import auth_service
from datetime import timedelta, datetime, timezone
from app.services import email_service
from django.contrib.auth.password_validation import validate_password


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
    def search_author(query):
        query = query.split('@')[0]
        authors = AuthorAccessor.search_author(query)
        if not authors:
            raise ValueError
        return authors

    @staticmethod
    def delete_author(id):
        post_business.Post.delete_posts_by_author(id)
        AuthorAccessor.delete_author(id)

    @staticmethod
    def login(email, password):
        author = AuthorAccessor.get_author_by_email(email=email)
        if not author:
            raise ValueError('Author does not exists')
        if not author.is_verified:
            raise ValueError('Author is not verified')
        is_valid = check_password(password=password, encoded=author.password)
        if not is_valid:
            raise ValueError
        token = auth_service.generate_token(author)
        return author, token

    @staticmethod
    def generate_and_send_otp(email):
        author = AuthorAccessor.get_author_by_email(email=email)
        if not author:
            raise ValueError('Author does not exists')
        email_service.generate_and_send_otp(author)

    @staticmethod
    def verify_otp(author, otp):
        is_valid = author.otp == otp and (
            datetime.now(timezone.utc) - author.otp_sent_at
        ) < timedelta(minutes=10)
        if not is_valid:
            raise ValueError('Invalid OTP')
        author = AuthorAccessor.verify_author(author)
        return author

    @classmethod
    def verify_email(cls, email, otp):
        author = AuthorAccessor.get_author_by_email(email=email)
        if not author:
            raise ValueError('Author does not exists')
        if author.is_verified:
            raise ValueError('Author is already verified')
        try:
            author_verified = cls.verify_otp(author, otp)
        except Exception as e:
            raise e

        return author_verified

    @classmethod
    def reset_password(cls, email, otp, password):
        author = AuthorAccessor.get_author_by_email(email=email)
        if not author:
            raise ValueError('Author does not exists')
        try:
            cls.verify_otp(author, otp)
        except Exception as e:
            raise e
        AuthorAccessor.update_password(author, password)

    @staticmethod
    def change_password(author, password):
        try:
            validate_password(password)
        except ValidationError as e:
            raise e
        AuthorAccessor.update_password(author, password)
        return author
