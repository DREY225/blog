from django.shortcuts import render
from django.http import HttpResponse
from main.models import Article

# Create your views here.

def index(request):
    
    articles = Article.objects.order_by("-created_at")[:3]
    context = {
        "articles" : articles
    }
    return render(request, "main/home.html", context)
    
def article(request):
    return HttpResponse("Liste des articles")
   