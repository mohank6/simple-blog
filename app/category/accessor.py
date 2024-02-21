from app.models import Category
from typing import Optional, List


class CategoryAccessor:

    @staticmethod
    def get_all_categories() -> Optional[List[Category]]:
        categories = Category.objects.all()
        return categories

    @staticmethod
    def get_category_by_name(name: str) -> Optional[Category]:
        category = Category.objects.filter(name=name).first()
        return category

    @staticmethod
    def get_category_by_id(id: str) -> Optional[Category]:
        category = Category.objects.filter(id=id).first()
        return category

    @staticmethod
    def delete_category(id: str) -> None:
        category = Category.objects.filter(id=id).first()
        category.delete()
