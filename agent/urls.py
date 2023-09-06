from django.urls import path
from agent.apps import AgentConfig
from agent.views import MailingListView, MailingCreateView, MailingUpdateView, MailingDetailView, MailingDeleteView

app_name = AgentConfig.name

urlpatterns = [
    path('', MailingListView.as_view(), name='mailing_list'),
    path('mailing_create/', MailingCreateView.as_view(), name='mailing_create'),
    path('mailing/<int:pk>/update/', MailingUpdateView.as_view(), name='mailing_update'),
    path('mailing/<int:pk>/detail/', MailingDetailView.as_view(), name='mailing_detail'),
    path('mailing/<int:pk>/delete/', MailingDeleteView.as_view(), name='mailing_delete'),
]
