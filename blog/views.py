from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from .models import Book, Writer, Translator, Post
from django.views import generic
import random
from django.template import Context, Template

# Random view

def random_post(request):
        post_count = Post.objects.all().count()  #Count the objects in Post
        random_val = random.randint(0, post_count-1)   #Pick a random number between 1 and the post_count - 1
        post_id = Post.objects.values_list('post_id', flat=True)[random_val]   #Set the post_id equal to random_val
        return redirect('post_detail', pk=post_id) #Ridirect to post detail

# Old school index
def index(request):
    return render(request, 'blog/index.html')

class HomePageView(TemplateView):
    template_name = "blog/home.html"    
    
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
    template_name = 'blog/book_list.html'
    
class BookDetailView(DetailView):
    model = Book
    template_name = 'blog/book_detail.html'
    
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
    
#Contact Form
def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['rr@ronraney.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "blog/contact.html", {'form': form})

def successView(request):
    return render(request, "blog/success.html")