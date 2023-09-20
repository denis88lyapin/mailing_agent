import random

from django.shortcuts import render

from agent.models import Mailing
from blog.models import Article
from blog.services import get_articles_cache


def home(request):
    mailing_count = Mailing.objects.all().count()
    mailing_active_count = Mailing.objects.filter(mailing_status=Mailing.STATUS_STARTED).count()
    articles_all = get_articles_cache()
    articles_count = len(articles_all)
    num_articles_to_display = min(3, articles_count)
    articles = random.sample(list(articles_all), num_articles_to_display)
    for article in articles:
        article.view_count += 1
        article.save()

    context = {
        'title': 'Главаная',
        'mailing_count': mailing_count,
        'mailing_active_count': mailing_active_count,
        'articles': articles
    }

    return render(request, 'blog/home.html', context)
