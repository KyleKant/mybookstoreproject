from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import ListView, UpdateView
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from django.db.models import Q


from .forms import CreateBookForm, ChapterForm
from .models import Book, Chapter
# Create your views here.


class BookListView(ListView):
    model = Book
    template_name = "home.html"
    context_object_name = 'books'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        kwargs['books'] = self.books
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        search_term = ''
        if 'search' in self.request.GET:
            search_term = self.request.GET['search']
            self.books = Book.objects.all().filter(
                Q(author__icontains=search_term) | Q(
                    name_book__icontains=search_term)
            )
        else:
            self.books = Book.objects.all()
        queryset = self.books.order_by('uploaded_at')
        return queryset


# def home(request):
#     search_term = ''
#     if 'search' in request.POST:
#         search_term = request.GET['search']
#         books = Book.objects.all().filter(name_book__icontains=search_term)
#     else:
#         books = Book.objects.all()
#     return render(request, 'home.html', {'books': books})


class MyBookListView(ListView):
    model = Book
    template_name = 'my_books.html'
    context_object_name = 'books'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        kwargs['books'] = self.books
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        if User.is_authenticated:
            self.books = Book.objects.filter(upload_by=self.request.user)
            # self.books = Book.objects.all()
            queryset = self.books.order_by('uploaded_at')
        return queryset

# def my_books(request):
#     if User.is_authenticated:
#         books = Book.objects.filter(upload_by=request.user)
#     return render(request, 'my_books.html', {'books': books})


def upload_book(request):
    # book = get_object_or_404(Book)
    if request.method == 'POST':
        form = CreateBookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            # form.save()
            Book.objects.create(
                name_book=form.cleaned_data.get('name_book'),
                slug=form.cleaned_data.get('slug'),
                author=form.cleaned_data.get('author'),
                illumination=form.cleaned_data.get('illumination'),
                upload_by=request.user,
                updated_by=request.user,
                status=form.cleaned_data.get('status'),
                category=form.cleaned_data.get('category'),
                content_summary=form.cleaned_data.get('content_summary'),

            )
            return redirect('my_books')
    else:
        form = CreateBookForm()
    return render(request, 'upload_book.html', {'form': form})


class ChapterListView(ListView):
    model = Chapter
    template_name = 'book_homepage.html'
    context_object_name = 'chapters'
    context_object_name = 'book'
    context_object_name = 'first_chapter'

    # context_object_name = 'chapters_count'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        kwargs['book'] = self.book
        kwargs['chapters'] = self.chapters
        kwargs['first_chapter'] = self.first_chapter
        kwargs['last_chapter'] = self.last_chapter
        # kwargs['chapters_count'] = self.chapters_count
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.book = get_object_or_404(Book, slug=self.kwargs.get('slug'))
        # self.chapters = get_object_or_404(Chapter, slug=self.kwargs.get('slug_chapter'))
        if User.is_authenticated:
            self.chapters = Chapter.objects.filter(book=self.book)
            self.first_chapter = self.chapters.first()
            self.last_chapter = self.chapters.last()
            queryset = self.chapters.order_by('created_by')
        return queryset
        # return Chapter.objects.filter(created_by=self.request.user)

# def book_homepage(request, name_book):
#     book = get_object_or_404(Book, name_book=name_book)
#     if User.is_authenticated:
#         chapters = Chapter.objects.filter(created_by=request.user, book=book)
#     return render(request, 'book_homepage.html', {'chapters': chapters, 'book': book})


class BookUpdateView(UpdateView):
    model = Book
    form_class = CreateBookForm
    template_name = 'update_book.html'
    context_object_name = 'book'
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(upload_by=self.request.user)

    def form_valid(self, form):
        book = form.save(commit=False)
        book.updated_by = self.request.user
        book.updated_at = timezone.now()
        book.save()
        return redirect('book_homepage', slug=book.slug)

# def update_book(request, name_book):
#     book = get_object_or_404(Book, name_book=name_book)
#     if User.is_authenticated:
#         if request.method == 'POST':
#             form = CreateBookForm(request.POST, instance=book)
#             if form.is_valid():
#                 book = form.save(commit=False)
#                 book.update_by = request.user
#                 book.updated_at = timezone.now()
#                 book.save()
#                 return redirect('book_homepage.html', name_book=name_book)
#         else:
#             form = CreateBookForm()

#     return render(request, 'update_book.html', {'book': book, 'form': form})


def upload_chapter(request, slug):
    book = get_object_or_404(Book, slug=slug)
    if request.method == 'POST':
        form = ChapterForm(request.POST)
        if form.is_valid():
            chapter = form.save(commit=False)
            chapter.book = book
            chapter.created_by = request.user
            chapter.update_by = request.user
            # chapter = form.save()
            Chapter.objects.create(
                name_chapter=form.cleaned_data.get('name_chapter'),
                # slug_chapter=form.cleaned_data.get('slug_chapter'),
                book=book,
                content_chapter=form.cleaned_data.get('content_chapter'),
                created_by=request.user,
                update_by=request.user
            )
            return redirect('book_homepage', slug=slug)
    else:
        form = ChapterForm()
    return render(request, 'upload_chapter.html', {'form': form, 'book': book})


# class ChapterContentListView(ListView):
#     model = Chapter
#     template_name = 'chapter_content.html'
#     context_object_name = 'chapters'
#     context_object_name = 'book'
#     context_object_name = 'previous_chapter'
#     paginate_by = 1

#     def get_context_data(self, **kwargs):
#         kwargs['chapters'] = self.chapters
#         kwargs['book'] = self.book
#         kwargs['previous_chapter'] = self.previous_chapter
#         return super().get_context_data(**kwargs)

#     # def get_previous_chapter(self, query, get_queryset):
#     #     for obj in get_queryset:
#     #         if obj == query:
#     #             break
#     #         previous_chapter = obj
#     #     return previous_chapter

#     def get_queryset(self):
#         self.book = get_object_or_404(Book, name_book=self.kwargs.get('name_book'))
#         self.chapters = get_object_or_404(Chapter, name_chapter=self.kwargs.get('name_chapter'))
#         queryset = Chapter.objects.filter(created_by=self.request.user, book=self.book).order_by('name_chapter')
#         self.previous_chapter = get_object_or_404(queryset, name_chapter=self.kwargs.get('name_chapter'))
#         return queryset

def chapter_content(request, slug, slug_chapter):
    book = get_object_or_404(Book, slug=slug)
    current_chapter = get_object_or_404(
        Chapter, book=book, slug_chapter=slug_chapter)
    if User.is_authenticated:
        chapters = Chapter.objects.filter(created_by=request.user, book=book)
    try:
        previous_chapter = current_chapter.get_previous_by_created_at(
            book=book)
    except Chapter.DoesNotExist:
        previous_chapter = current_chapter
    try:
        next_chapter = current_chapter.get_next_by_created_at(book=book)
    except Chapter.DoesNotExist:
        next_chapter = current_chapter
    return render(request, 'chapter_content.html', {
        'current_chapter': current_chapter,
        'book': book,
        'previous_chapter': previous_chapter,
        'next_chapter': next_chapter,
        'chapters': chapters,
    })


class ChapterUpdateView(UpdateView):
    model = Chapter
    form_class = ChapterForm
    template_name = 'edit_chapter.html'
    context_object_name = 'chapter'
    # context_object_name = 'book'
    slug_field = 'slug_chapter'
    slug_url_kwarg = 'slug_chapter'

    def get_context_data(self, **kwargs):
        kwargs['book'] = self.book
        kwargs['chapter'] = self.chapter
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.book = get_object_or_404(Book, slug=self.kwargs.get('slug'))
        self.chapter = get_object_or_404(
            Chapter, book=self.book, slug_chapter=self.kwargs.get('slug_chapter'))
        queryset = super().get_queryset()
        return queryset.filter(created_by=self.request.user, book=self.book)

    def form_valid(self, form):
        chapter = form.save(commit=False)
        chapter.update_by = self.request.user
        chapter.updated_at = timezone.now()
        chapter.save()
        return redirect('chapter_content', slug=chapter.book.slug, slug_chapter=chapter.slug_chapter)

# def edit_chapter(request, slug, slug_chapter):
#     book = get_object_or_404(Book, slug=slug)
#     chapter = get_object_or_404(Chapter, slug=slug_chapter)
#     if request.method == 'POST':
#         form = ChapterForm(request.POST, instance=chapter)
#         if form.is_valid():
#             chapter = form.save(commit=False)
#             chapter.update_by = request.user
#             chapter.updated_at = timezone.now()
#             chapter.save()

#             return redirect('chapter_content', slug=slug, slug_chapter=slug_chapter)
#     else:
#         form = ChapterForm()
#     return render(request, 'edit_chapter.html', {'form': form, 'book': book, 'chapter': chapter})
