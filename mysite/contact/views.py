from django.shortcuts import render
from django.views.generic import DetailView, FormView

from contact.forms import MessageForm, ContactForm
from .models import Message

class MessageDetailView(DetailView):
    model = Message


class MessageAddView(FormView):
    # form_class = MessageForm
    form_class = ContactForm
    template_name = 'contact/message_form.html'
    success_url = '/'

    # def form_valid(self, form): #uruchamiana gry formularz jest poprwanie wprowadzony
    #     form.save() # bo form jest instacja ModelForm, ktory posiada moetode save()
    #     #save - wprowadza dane z formularza do bazy danych - w nasz model
    #     return super(MessageAddView, self).form_valid(form)
    # odwolenie do klasy nadrzednej, ktora wysyla Httprequest o przekierowanie
    # do success_url