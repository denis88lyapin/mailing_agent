from django import forms

from agent.models import Mailing, Client


class VisualMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class MailingForm(VisualMixin, forms.ModelForm):
    class Meta:
        model = Mailing
        fields = '__all__'


class ClientForm(VisualMixin, forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
