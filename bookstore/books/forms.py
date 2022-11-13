from django import forms
from .models import Book, Chapter


class CreateBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name_book', 'author', 'illumination', 'category', 'content_summary', 'status')


class ChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ('name_chapter', 'content_chapter')
