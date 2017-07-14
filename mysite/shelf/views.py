from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView
from .models import Author, Book


class ShelfIndexView(TemplateView):
    template_name = 'shelf/shelf_index.html'


# class ShelfIndexView(View):
#     def get(self, request, *args, **kwargs):
#         return HttpResponse('OK - klasa')

    #get/post/tutaj definiuje sie metody, ktore zostana
        #wywoalne zalzenie od otrzymanego zapytania
    #def post(self):

index_view = ShelfIndexView.as_view()
#korzystajac z powyzszej metody mozemy ja przekzac do url i
#nie importowac przy tym zadnych klas -- plik url jest mniejszy


# def index_view(request, *args, **kwargs):
#     return HttpResponse('OK - funkcja')


class AuthorListView(ListView):
    model = Author


class AuthorDetailView(DetailView):
    model = Author


class BookListView(ListView):
    model = Book


class BookDetailView(DetailView):
    model = Book

