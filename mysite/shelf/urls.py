from django.conf.urls import url
from shelf.views import AuthorListView, AuthorDetailView, BookListView, BookDetailView

# app_name = 'shelf'
urlpatterns = [
    url(r'^authors/$', AuthorListView.as_view(), name='author-list'),
    url(r'^authors/(?P<pk>\d+)/$', AuthorDetailView.as_view(), name='author-detail'),
    url(r'^books/$', BookListView.as_view(), name='book-list'),
    url(r'^books/(?P<pk>\d+)/$', BookDetailView.as_view(), name='book-detail'),
]
