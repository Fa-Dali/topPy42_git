from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

def index(request):
    return HttpResponse("Hello, world!")

# Главная страница
def home(request):
    return render(request, 'home.html')

# Раздел "Новости города"
def news(request):
    return render(request, 'news.html')

# Раздел "Руководство города"
def management(request):
    return render(request, 'management.html')

# Раздел "Факты о городе"
def facts(request):
    return render(request, 'facts.html')

# Раздел "Контактные телефоны городских служб"
def contacts(request):
    return render(request, 'contacts.html')

# Основная страница истории
def history(request):
    return render(request, 'history.html')

# Подраздел "Известные жители"
def people(request):
    return render(request, 'people.html')

# Подраздел "Исторические фотографии"
def photos(request):
    return render(request, 'photos.html')

# Подраздел "Видео"
def videos(request):
    current_datetime = datetime.now()
    return render(request, 'videos.html', {'current_datetime': current_datetime})