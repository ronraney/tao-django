from django.urls import path
from django.contrib import admin
from django.contrib.flatpages import views as flat_views
from django.conf.urls.static import static
from django.conf import settings
from . import views   


urlpatterns = [
    path('', views.index, name='index'),
    path('success/', views.successView, name='success'),
    path('home/', views.HomePageView.as_view(), name='home'),
    path('posts/', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/random/', views.random_post, name='random_post'),
    path('tao/', flat_views.flatpage, {'url': '/tao/'}, name='tao'),
    path('recovery/', flat_views.flatpage, {'url': '/recovery/'}, name='recovery'),
    path('taorecovery/', flat_views.flatpage, {'url': '/taorecovery/'}, name='taorecovery'),
    path('mission/', flat_views.flatpage, {'url': '/mission/'}, name='mission'),
    path('resources/', flat_views.flatpage, {'url': '/resources/'}, name='resources'),
    path('books', views.BookListView.as_view(), name='books'),
    path('book/<int:book_id>/', views.BookDetailView.as_view(), name='book-detail'),
    path('writers', views.WriterListView.as_view(), name='writers'),
    path('writer/<int:writer_id>/', views.WriterDetailView.as_view(), name='writer-detail'),
    path('translators', views.TranslatorListView.as_view(), name='translators'),
    path('translator/<int:translator_id>/', views.TranslatorDetailView.as_view(), name='translator-detail'),
    path('contact/', views.emailView, name='contact'),
    path('success/', views.successView, name='success'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)