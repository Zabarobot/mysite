from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
from django.utils.timezone import now

from shelf.models import BookItem


class Rental(models.Model):
    who = models.ForeignKey(User)
    what = models.ForeignKey(BookItem)
    when = models.DateTimeField(default=now)
    returned = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "{what.__str__()}, {when}, {returned}".format(what=self.what,
                                                             when=self.when,
                                                             returned=self.returned)

    # auto_now_add=True - dodaje date automatycznie przy oddaniu wpisu
    #auto_now - aktualizuje date przy okazji kazdej zmiany wpisu
    #ale pola takiego nie mozemy sami edytowac
    #2 metoda:
    #default=datetime.now() - ale to ustawia czas uruchomienia aplikacji
    #3 metoda:
    #wykorzystana tutaj, biblioteka timezone ^^

    #null=True - baza danych wie, ze pole moze byc puste(nie ustawiac przy charfieldach)
    #blank=True - frontend wie, ze pole moze byc puste
