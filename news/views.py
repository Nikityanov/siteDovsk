from django.shortcuts import render
from .models import Articles
from django.views.generic import DetailView

def news(request):
    news = Articles.objects.order_by('-date')
    # data = {'title': 'Новости'}
    return render(request, 'news/news.html', {'news':news})


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'