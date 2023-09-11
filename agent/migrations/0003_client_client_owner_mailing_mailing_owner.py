# Generated by Django 4.2.5 on 2023-09-11 17:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('agent', '0002_alter_mailing_mailing_clients'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='client_owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='продавец'),
        ),
        migrations.AddField(
            model_name='mailing',
            name='mailing_owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='продавец'),
        ),
    ]
