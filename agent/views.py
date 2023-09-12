from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from agent.form import MailingForm, ClientForm
from agent.models import Mailing, Client


class MailingListView(ListView):
    model = Mailing
    extra_context = {
        'title': 'Рассылки'
    }

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            queryset = super().get_queryset()
        else:
            queryset = super().get_queryset().filter(
                mailing_owner=user.pk
            )
        return queryset


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


class MailingUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Mailing
    form_class = MailingForm
    extra_context = {
        'title': 'Изменение рассылки'
    }

    def test_func(self):
        user = self.request.user
        mailing = self.get_object()

        if mailing.mailing_owner == user or user.is_staff:
            return True
        return False

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.mailing_owner != self.request.user and not self.request.user.is_superuser:
            raise Http404
        return self.object

    def handle_no_permission(self):
        return redirect(reverse_lazy('agent:mailing_list'))

    def get_success_url(self):
        return reverse('agent:mailing_detail', args=[self.object.pk])


class MailingDetailView(DetailView, UserPassesTestMixin):
    model = Mailing
    extra_context = {
        'title': 'Информация о рассылке'
    }

    def test_func(self):
        user = self.request.user
        mailing = self.get_object()

        if mailing.mailing_owner == user or user.is_staff:
            return True
        return False

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.mailing_owner != self.request.user and not self.request.user.is_superuser:
            raise Http404
        return self.object

    def handle_no_permission(self):
        return redirect(reverse_lazy('agent:mailing_list'))


class MailingDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Mailing
    success_url = reverse_lazy('agent:mailing_list')
    extra_context = {
        'title': 'Удаление рассылки'
    }

    def test_func(self):
        user = self.request.user
        mailing = self.get_object()

        if mailing.mailing_owner == user or user.is_superuser:
            return True
        return False

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.mailing_owner != self.request.user and not self.request.user.is_superuser:
            raise Http404
        return self.object

    def handle_no_permission(self):
        return redirect(reverse_lazy('agent:mailing_list'))


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


