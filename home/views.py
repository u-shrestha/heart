from django.shortcuts import render
from .models import Article
from .models import Doctor, Hospital
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    return render(request, 'home/home.html')


def blog(request):
    article_list = Article.objects.all()
    paginator = Paginator(article_list, 6)
    page = request.GET.get('page')
    article_list_filter = paginator.get_page(page)
    article_dict = {'article_list_filter': article_list_filter}
    return render(request, 'home\\blog.html', article_dict)


def blog_detail(request, article_id):
    detail = Article.objects.get(pk=article_id)
    return render(request, 'home\\blog_detail.html', {'detail': detail})


def doctor(request):
    dlist = Doctor.objects.all()
    return render(request, 'home\doctor.html', {'dlist': dlist})

def hospital(request):
    hlist = Hospital.objects.all()
    return render(request, 'home\hospital.html', {'hlist': hlist})