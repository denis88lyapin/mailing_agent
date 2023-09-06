from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from agent.form import MailingForm, ClientForm
from agent.models import Mailing, Client


class MailingListView(ListView):
    model = Mailing
    extra_context = {
        'title': 'Мои рассылки'
    }


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    extra_context = {
        'title': 'Добавление рассылки'
    }

    def get_success_url(self):
        return reverse('agent:mailing_detail', args=[self.object.pk])


class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingForm
    extra_context = {
        'title': 'Изменение рассылки'
    }

    def get_success_url(self):
        return reverse('agent:mailing_detail', args=[self.object.pk])


class MailingDetailView(DetailView):
    model = Mailing
    extra_context = {
        'title': 'Информация о рассылке'
    }


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('agent:mailing_list')
    extra_context = {
        'title': 'Удаление рассылки'
    }


class ClientListView(ListView):
    model = Client
    extra_context = {
        'title': 'Мои клиенты'
    }


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    extra_context = {
        'title': 'Добавление клиента'
    }

    def get_success_url(self):
        return reverse('agent:client_detail', args=[self.object.pk])


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    extra_context = {
        'title': 'Изменение клиента'
    }

    def get_success_url(self):
        return reverse('agent:client_detail', args=[self.object.pk])


class ClientDetailView(DetailView):
    model = Client
    extra_context = {
        'title': 'Информация о клиенте'
    }


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('agent:client_list')
    extra_context = {
        'title': 'Удаление клиента'
    }
