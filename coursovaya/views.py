from django.core.files.base import ContentFile
from uuid import uuid4

from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
import base64
from coursovaya.forms import RegistrationForm, LoginForm
from coursovaya.models import UserRegistration, Log
from coursovaya.utils import classify_face
import face_recognition_models

# Create your views here.

def index_whit_authorization(request):
    return render(request, "index_whit_authorization.html")


def authorization(request):
    return render(request, "authorization.html")


@login_required
def clas(request):
    return render(request, "class.html")


@login_required
def constructor(request):
    return render(request, "constructor.html")


@login_required
def history(request):
    return render(request, "history.html")


@login_required
def index(request):
    return render(request, "index.html")


@login_required
def modernrobot(request):
    return render(request, "modernrobot.html")


@login_required
def robototex(request):
    return render(request, "robototex.html")


def entrance(request):
    return render(request, "entrance.html")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def register_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = form.cleaned_data['password']  # можно захешировать пароль, если нужно
            user.verification_code = uuid4()  # создаем код подтверждения
            user.save()

            # Отправка email с кодом подтверждения
            send_mail(
                "Подтверждение регистрации",
                f"Ваш код подтверждения: {user.verification_code}",
                settings.EMAIL_HOST_USER,
                [user.email],
                fail_silently=False,
            )

            return redirect("check_verification", user_id=user.id)
    else:
        form = RegistrationForm()
    return render(request, "register.html", {"form": form})


def check_verification(request, user_id):
    if request.method == "POST":
        verification_code = request.POST.get("verification_code")
        try:
            registration = UserRegistration.objects.get(id=user_id, verification_code=verification_code)
            registration.is_verified = True
            registration.save()
            user = User.objects.create_user(
                username=registration.username,
                email=registration.email,
                password=registration.password,
            )

            # Сохранение изображения профиля
            user.profile.image = registration.image  # теперь у профиля есть поле image
            user.profile.save()

            return redirect("login")  # Перенаправление на страницу входа после успешного подтверждения
        except UserRegistration.DoesNotExist:
            return render(request, "verification_failed.html", {"error": "Неверный код подтверждения"})

    return render(request, "check_verification.html")


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("index")  # перенаправление на главную страницу или профиль
            else:
                return render(request, "login.html", {"form": form, "error": "Неверные данные для входа"})
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})


def get_user_by_face(image_data: str):

    decoded_file = base64.b64decode(image_data)
    x = Log()
    x.photo.save('upload.png', ContentFile(decoded_file))
    x.save()
    res = classify_face(x.photo.path)
    if res:
        user_exists = User.objects.filter(username=res).exists()
        if user_exists:
            return User.objects.get(username=res)
    return None


def faceid_login(request):
    if request.method == "POST":
        # Предполагаем, что фронтенд отправляет изображение в формате Base64
        image_data = request.POST.get("face_image")

        # Пример обработки: сравнить изображение с базой данных лиц пользователей
        # Здесь вам нужно подключить алгоритм для сравнения лиц
        user = get_user_by_face(image_data)  # Этот метод должен проверять лицо пользователя и возвращать объект User, если найдено совпадение.
        if user:
            login(request, user)
            return JsonResponse({"status": "success", "message": "Вход по FaceID успешен."})
        else:
            return JsonResponse({"status": "error", "message": "Лицо не распознано."})

    return JsonResponse({"status": "error", "message": "Неверный метод запроса."})
