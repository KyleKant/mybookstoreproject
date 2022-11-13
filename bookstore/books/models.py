from django.db import models
from django.contrib.auth.models import User
from markdown import markdown
from django.utils.html import mark_safe
from django.utils.text import Truncator
# from django.template.defaultfilters import slugify
from autoslug import AutoSlugField
# from django_resized import ResizedImageField

# Create your models here.


class Book(models.Model):
    """
    Description: Model Description
    """

    # def upload_image(self, filename):
    #     self.name_book = "_".join(self.name_book.split())
    #     return 'book_illu/{}/{}'.format(self.name_book, filename)

    name_book = models.CharField(max_length=30)
    slug = AutoSlugField(populate_from='name_book', editable=True)
    author = models.CharField(max_length=30)
    illumination = models.ImageField(
        height_field='img_height', width_field='img_width')
    img_height = models.IntegerField()
    img_width = models.IntegerField()
    upload_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='books')
    updated_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='+')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    category = models.CharField(max_length=100)
    content_summary = models.TextField()
    status = models.CharField(max_length=30)

    def __str__(self):
        return '{}'.format(self.name_book)
        pass

    def get_content_summary_as_markdown(self):
        return mark_safe(markdown(self.content_summary, safe_mode='escape'))

    def get_chapters_count(self):
        return Book.objects.filter(chapters__book=self).count()
        pass

    class Meta:
        pass


class Chapter(models.Model):
    """
    Description: Model Description
    """
    name_chapter = models.CharField(max_length=100)
    slug_chapter = AutoSlugField(populate_from='name_chapter', editable=True)
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name='chapters')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='chapters')
    updated_at = models.DateTimeField(null=True)
    update_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='+')
    content_chapter = models.TextField()

    def __str__(self):
        return self.name_chapter
        pass

    def get_content_as_markdown(self):
        return mark_safe(markdown(self.content_chapter, safe_mode='escape'))

    class Meta:
        pass


class Category(models.Model):
    """
    Description: Model Description
    """
    name_category = models.CharField(max_length=30)
    book = models.ManyToManyField(Book, related_name='categories')

    class Meta:
        pass


class Content_Chapter(models.Model):
    """
    Description: Model Description
    """
    chapter = models.ForeignKey(
        Chapter, on_delete=models.CASCADE, related_name='content_chapters')
    last_updated = models.DateTimeField(auto_now_add=True)
    content_chapter = models.TextField()

    def __str__(self):
        return str(self.chapter)
        pass

    class Meta:
        pass
