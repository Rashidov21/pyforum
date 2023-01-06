from django.db import models
from accounts.models import User
# Create your models here.

from django_quill.fields import QuillField


class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = 'Categories'


class Tag(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return str(self.name)


class Topic(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    body = QuillField()
    top = models.BooleanField(default=False)
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name='category')
    tag = models.ForeignKey(
        Tag, on_delete=models.PROTECT, related_name='tag')
    published = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='topics')

    def __str__(self):
        return str(self.title)


class Comment(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = QuillField()

    def __str__(self):
        return str(self.user.username)
