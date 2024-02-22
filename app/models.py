from django.db import models
from app.utils.utils import get_char_uuid


# db_index=True
# objects = models.Manager()
class BaseModel(models.Model):
    id = models.CharField(
        primary_key=True,
        max_length=100,
        db_index=True,
        editable=False,
        default=get_char_uuid,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    class Meta:
        abstract = True


class Author(BaseModel):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Category(BaseModel):

    TECHNOLOGY = "Technology"
    LIFESTYLE = "Lifestyle"
    BUSINESS = "Business"
    SCIENCE = "Science"
    ENTERTAINMENT = "Entertainment"
    EDUCATION = "Education"
    SPORTS = "Sports"
    TRAVEL = "Travel"
    OTHER = "Other"

    CATEGORY_CHOICES = (
        (TECHNOLOGY, "Technology and Gadgets"),
        (LIFESTYLE, "Lifestyle and Fashion"),
        (BUSINESS, "Business and Entrepreneurship"),
        (SCIENCE, "Science and Innovation"),
        (ENTERTAINMENT, "Entertainment and Pop Culture"),
        (EDUCATION, "Education and Learning"),
        (SPORTS, "Sports and Fitness"),
        (TRAVEL, "Travel and Adventure"),
        (OTHER, "Other"),
    )
    name = models.CharField(max_length=255, unique=True, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Post(BaseModel):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField()
    categories = models.ManyToManyField(Category, related_name='posts')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    is_published = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Comment(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=255)
    email = models.EmailField()
    content = models.TextField()
    is_approved = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} commented {self.content}"

    class Meta:
        unique_together = ['post', 'email']
