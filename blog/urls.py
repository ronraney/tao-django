from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.PostListView.as_view(), name='post_list'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    #path('tao/', views.tao name='tao'),
    #path('recovery/', views.recovery, name='recovery'),
    #path('taorecovery/', views.taorecovery, name='taorecovery'),
    #path('contact/', views.contact, name='contact'),
    #path('resources/', views.resources, name='resources'),
    path('books', views.BookListView.as_view(), name='books'),
    path('book/<int:book_id>/', views.BookDetailView.as_view(), name='book-detail'),
    path('writers', views.WriterListView.as_view(), name='writers'),
    path('writer/<int:writer_id>/', views.WriterDetailView.as_view(), name='writer-detail'),
    path('translators', views.TranslatorListView.as_view(), name='translators'),
    path('translator/<int:translator_id>/', views.TranslatorDetailView.as_view(), name='translator-detail'),
]