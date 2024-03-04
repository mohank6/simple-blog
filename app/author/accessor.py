from app.models import Author
from typing import Optional, List


class AuthorAccessor:

    @staticmethod
    def get_author_by_id(id: str) -> Optional[Author]:
        author = Author.objects.filter(id=id, is_active=True).first()
        return author

    @staticmethod
    def get_all_authors() -> Optional[List[Author]]:
        authors = Author.objects.filter(is_active=True).all()
        return authors

    @staticmethod
    def delete_author(id: str) -> None:
        author = Author.objects.filter(id=id).first()
        author.is_active = False
        author.save()

    @staticmethod
    def get_author_by_email(email: str) -> Optional[Author]:
        author = Author.objects.filter(email__iexact=email).first()
        return author

    @staticmethod
    def verify_author(author: Author) -> Optional[Author]:
        author.otp = None
        author.is_verified = True
        author.save()
        return author

    @staticmethod
    def update_password(author: Author, password: str) -> Optional[Author]:
        author.password = password
        author.save()
        return author
