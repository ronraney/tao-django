from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Book, Writer, Translator, Post

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')
    
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
    
from django.views import generic

class BookListView(generic.ListView):
    model = Book
    paginate_by = 20
    
class BookDetailView(generic.DetailView):
    model = Book
    
class WriterListView(generic.ListView):
    model = Writer
    paginate_by = 20
    
class WriterDetailView(generic.DetailView):
    model = Writer
    
class TranslatorListView(generic.ListView):
    model = Translator
    paginate_by = 20
    
class TranslatorDetailView(generic.DetailView):
    model = Translator