from app.category.accessor import CategoryAccessor


class Category:

    @staticmethod
    def get_all_categories():
        categories = CategoryAccessor.get_all_categories()
        if not categories:
            raise ValueError
        return categories

    @staticmethod
    def get_category_by_id(id):
        category = CategoryAccessor.get_category_by_id(id)
        if not category:
            raise ValueError
        return category

    @staticmethod
    def get_category_by_name(name):
        category = CategoryAccessor.get_category_by_name(name)
        if not category:
            raise ValueError
        return category

    @staticmethod
    def delete_category(id):
        try:
            CategoryAccessor.delete_category(id)
        except Exception as e:
            raise e
