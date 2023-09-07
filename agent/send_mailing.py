import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

import datetime
from smtplib import SMTPException
from django.core.mail import send_mail
from decouple import config
from agent.models import Mailing, MailingLog
import pytz


def send_mails():
    now = datetime.datetime.now()
    for mailing in Mailing.objects.filter(mailing_status=Mailing.STATUS_STARTED):
        for mailing_client in mailing.mailing_clients.all():
            mailing_log = MailingLog.objects.filter(log_client=mailing_client, log_mailing=mailing)
            if mailing_log.exists():
                last_try = mailing_log.order_by('-created_time').first()
                desired_timezone = pytz.timezone('Europe/Moscow')
                last_try_date = last_try.created_time.astimezone(desired_timezone)
                if mailing.PERIOD_DAILY:
                    if (now.date() - last_try_date.date()).days >= 1:
                        send_email(mailing, mailing_client)
                elif mailing.PERIOD_WEEKLY:
                    if (now.date() - last_try_date.date()).days >= 7:
                        send_email(mailing, mailing_client)
                elif mailing.PERIOD_MONTHLY:
                    if (now.date() - last_try_date.date()).days >= 30:
                        send_email(mailing, mailing_client)
            else:
                send_email(mailing, mailing_client)


def send_email(mailing, mailing_client):
    subject = mailing.subject
    message = mailing.body
    from_email = config('EMAIL_HOST_USER')
    recipient_list = [mailing_client.email]
    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=from_email,
            recipient_list=recipient_list,
            fail_silently=False,
        )
        MailingLog.objects.create(
            log_status=MailingLog.STATUS_OK,
            log_client=mailing_client,
            log_mailing=mailing,
            response='отправлено'
        )

    except SMTPException as e:
        MailingLog.objects.create(
            log_status=MailingLog.STATUS_FAILED,
            log_client=mailing_client,
            log_mailing=mailing,
            response=e
        )


if __name__ == '__main__':
    send_mails()
