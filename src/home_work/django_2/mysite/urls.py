"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from helloapp.views import (
    home, news, management, facts, contacts,
    history, people, photos, videos
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Маршруты с поддержкой произвольных суффиксов
    re_path(r'^$', home, name='home'),
    re_path(r'^news/?$', news, name='news'),               # Удалены группы из регулярного выражения
    re_path(r'^management/?$', management, name='management'),
    re_path(r'^facts/?$', facts, name='facts'),
    re_path(r'^contacts/?$', contacts, name='contacts'),

    # Новая секция "История" с возможностью расширения
    re_path(r'^history/?$', history, name='history'),
    re_path(r'^history/people/?$', people, name='people'),
    re_path(r'^history/photos/?$', photos, name='photos'),
    re_path(r'^history/videos/?$', videos, name='videos'),
]
