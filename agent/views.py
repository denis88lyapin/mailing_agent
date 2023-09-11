from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from agent.form import MailingForm, ClientForm
from agent.models import Mailing, Client


class MailingListView(ListView):
    model = Mailing
    extra_context = {
        'title': 'Мои рассылки'
    }


class MailingCreateView(LoginRequiredMixin, CreateView):
    model = Mailing
    form_class = MailingForm
    extra_context = {
        'title': 'Добавление рассылки'
    }

    def get_success_url(self):
        return reverse('agent:mailing_detail', args=[self.object.pk])

    def form_valid(self, form):
        self.object = form.save()
        self.object.mailing_owner = self.request.user
        self.object.save()
        return redirect(self.get_success_url())


class MailingUpdateView(LoginRequiredMixin, UpdateView):
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


class MailingDeleteView(LoginRequiredMixin, DeleteView):
    model = Mailing
    success_url = reverse_lazy('agent:mailing_list')
    extra_context = {
        'title': 'Удаление рассылки'
    }


class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    extra_context = {
        'title': 'Мои клиенты'
    }


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    extra_context = {
        'title': 'Добавление клиента'
    }

    def get_success_url(self):
        return reverse('agent:client_detail', args=[self.object.pk])

    def form_valid(self, form):
        self.object = form.save()
        self.object.client_owner = self.request.user
        self.object.save()
        return redirect(self.get_success_url())


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    extra_context = {
        'title': 'Изменение клиента'
    }

    def get_success_url(self):
        return reverse('agent:client_detail', args=[self.object.pk])


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    extra_context = {
        'title': 'Информация о клиенте'
    }


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('agent:client_list')
    extra_context = {
        'title': 'Удаление клиента'
    }
