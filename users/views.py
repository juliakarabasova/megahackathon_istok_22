from datetime import datetime

from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.views.generic import CreateView

from appointments.models import Appointment
from users.forms import CustomUserCreationForm
from users.models import CustomUser
from django.contrib.auth import login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
import json
import logging

logger = logging.getLogger(__name__)

User = get_user_model()


@csrf_exempt
def create_or_login_user(request):
    logger.info("Получен запрос на создание/авторизацию пользователя")
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            phone_number = data.get('phone_number')
            code = data.get('code')

            logger.info(f"Полученные данные: телефон - {phone_number}, код - {code}")

            # Проверка существования пользователя
            user, created = User.objects.get_or_create(
                username=phone_number,
                defaults={'phone_number': phone_number}
            )

            if created:
                logger.info(f"Создан новый пользователь с телефоном {phone_number}")
                # Если пользователь новый, устанавливаем пароль
                password = str(code)
                user.set_password(password)
                user.save()
            else:
                logger.info(f"Найден существующий пользователь с телефоном {phone_number}")

            # Проверка пароля (кода)
            if user.check_password(code):
                login(request, user)
                logger.info(f"Пользователь {phone_number} успешно авторизован")
                return JsonResponse({'success': True})
            else:
                logger.warning(f"Неверный код для пользователя {phone_number}")
                return JsonResponse({'success': False, 'error': 'Неверный код'})
        except json.JSONDecodeError:
            logger.error("Ошибка при декодировании JSON")
            return JsonResponse({'success': False, 'error': 'Неверный формат данных'})
        except Exception as e:
            logger.error(f"Неожиданная ошибка: {str(e)}")
            return JsonResponse({'success': False, 'error': 'Произошла ошибка на сервере'})

    logger.warning("Получен неверный метод запроса")
    return JsonResponse({'success': False, 'error': 'Неверный метод запроса'})


class SignUp(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    success_url = '/accounts/login'
    template_name = 'registration/signup.html'


@require_http_methods(["GET", "POST"])
def personal_account_profile(request):
    user = request.user
    nearest_appointment = Appointment.objects.filter(user=user, date_time__gte=datetime.now()).order_by(
        'date_time').first()

    if request.method == 'POST':
        user.first_name = request.POST.get('first_name', '')
        user.second_name = request.POST.get('second_name', '')
        user.third_name = request.POST.get('third_name', '')
        user.phone_number = request.POST.get('phone_number', '')
        user.email = request.POST.get('email', '')
        user.save()
        return JsonResponse({'success': True})

    context = {
        'user': user,
        'nearest_appointment': nearest_appointment,
    }
    return render(request, 'personalAccountProfile.html', context)