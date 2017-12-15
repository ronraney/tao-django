from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from django.utils import timezone

from .models import Book, Writer, Translator, Post

# Old school index
def index(request):
    return render(request, 'blog/index.html')
    
# Generic Views
    
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class BookListView(ListView):
    model = Book
    paginate_by = 20
    
class BookDetailView(DetailView):
    model = Book
    
class WriterListView(ListView):
    model = Writer
    paginate_by = 20
    
class WriterDetailView(DetailView):
    model = Writer
    
class TranslatorListView(ListView):
    model = Translator
    paginate_by = 20
    
class TranslatorDetailView(DetailView):
    model = Translator
    
