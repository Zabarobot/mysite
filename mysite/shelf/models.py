from django.db import models
from django.core.urlresolvers import reverse_lazy


class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=50)

    def __str__(self): ##zwraca nam stringa - nazw; ustawia nazwa w bazie
        return "{first_name} {last_name}".format(first_name=self.first_name,
                                                 last_name=self.last_name)
    # formatowanie? ? ? ? ?


class Publisher(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name


class BookCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    cos w rodzaju rekopisu
    """
    title = models.CharField(max_length=100)  #pole znakowe
    authors = models.ManyToManyField(Author)
    # author = models.ForeignKey('Author')
    categories = models.ManyToManyField(BookCategory)

    def __str__(self):
        return self.title

    def get_absolute_url(self): #funkcja zamienia nazwe widoku na konkretna sciezke
        return reverse_lazy('shelf:book-detail', kwargs={'pk': self.id})
#lazy wykonywane jest kiedy absolutnie trzeba

class BookEdition(models.Model):
    """
    WYDANIE DANEJ KSIAZKI
    """
    book = models.ForeignKey(Book, related_name='editions')
    isbn = models.CharField(max_length=17)
    publisher = models.ForeignKey('Publisher')
    date = models.DateField()

    def __str__(self):
        return "{book.title}, {publisher.name}".format(book=self.book,
                                                        publisher=self.publisher)

COVER_TYPES = (
    ('soft', 'Sofr'),
    ('hard', 'Hard'),
    #(wartosc w bazie, wartosc wyswietlana)


)


class BookItem(models.Model):
    """
    KONKRETNY EGZEMPLARZ
    """
    edition = models.ForeignKey(BookEdition)
    catalogue_number = models.CharField(max_length=30)
    cover_type = models.CharField(max_length=4, choices=COVER_TYPES)

    def __str__(self):
        return "{edition}, {cover}".format(edition=self.edition,
                                           cover=self.get_cover_type_display())
    #getcoverdispley = getFOOdisplay odnosi sie do choices, pobiera ona wartosc jaka jest w bazie
    #i oddaje nam przypisana do niej wartosc do wyswietlania (u nas z COVER_TYPES