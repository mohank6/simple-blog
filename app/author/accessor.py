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
