"""
URL configuration for course project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import handler404
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from coursovaya import views


handler404 = views.pageNotFound

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_whit_authorization, name='Добро пожаловать на сайт!' ),
    path('authorization', views.authorization, name='Регистрация'),
    path('clas', views.clas, name='Важнейшие классы роботов'),
    path('constructor', views.constructor, name='Конструкторы программируемых роботов'),
    path('history', views.history, name='История развития робототехники'),
    path('index', views.index, name='Мир роботов'),
    path('modernrobot', views.modernrobot, name='Современные роботы'),
    path('robototex', views.robototex, name='Робототехника'),
    path('entrance', views.entrance, name='Вход'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

