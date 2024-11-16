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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from coursovaya import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_whit_authorization, name=''),
    # path('authorization', views.authorization, name='Регистрация'),
    path('class/', views.clas, name='class'),
    path('constructor/', views.constructor, name='constructor'),
    path('history/', views.history, name='history'),
    path('index/', views.index, name='index'),
    path('modernrobot/', views.modernrobot, name='modernrobot'),
    path('robototex/', views.robototex, name='robototex'),
    # path('entrance', views.entrance, name='Вход'),
    path("register/", views.register_view, name="register"),
    path("check-verification/<int:user_id>/", views.check_verification, name="check_verification"),
    path("login/", views.login_view, name="login"),
    path("faceid-login/", views.faceid_login, name="faceid_login"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
