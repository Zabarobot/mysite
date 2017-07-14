from django.conf.urls import url
from shelf.views import AuthorListView, AuthorDetailView, BookListView, BookDetailView, ShelfIndexView
from . import views

# app_name = 'shelf'
urlpatterns = [
    # url(r'^$', ShelfIndexView.as_view(), name='shelf-index'),
    url(r'^$', views.index_view, name='shelf-index'),
    url(r'^authors/$', AuthorListView.as_view(), name='author-list'),
    url(r'^authors/(?P<pk>\d+)/$', AuthorDetailView.as_view(), name='author-detail'),
    url(r'^books/$', BookListView.as_view(), name='book-list'),
    url(r'^books/(?P<pk>\d+)/$', BookDetailView.as_view(), name='book-detail'),
]
