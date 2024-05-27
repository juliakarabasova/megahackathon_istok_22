### Создание функционального блока User в Django

Для реализации функционального блока пользователей (Users) нам нужно:

1. **Создать модели**: Мы уже сделали это.
2. **Настроить формы**: Для регистрации, авторизации и управления пользователями.
3. **Настроить представления (views)**: Для отображения форм и обработки данных.
4. **Настроить URL-ы**: Для маршрутизации запросов.
5. **Создать шаблоны (templates)**: Для отображения форм и страниц пользователя.

### 1. Настройка форм

Создадим формы для регистрации и редактирования профиля.

**users/forms.py**:
```python
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'loyalty_points', 'referral_code')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'loyalty_points', 'referral_code')
```

### 2. Настройка представлений (views)

Создадим представления для регистрации, авторизации, профиля и редактирования профиля.

**users/views.py**:
```python
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomUserChangeForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'users/edit_profile.html', {'form': form})
```

### 3. Настройка URL-ов

**users/urls.py**:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
]
```

### 4. Настройка основного URL-скрипта

Подключим URL-ы приложения `users` в основном URL-скрипте.

**istok/urls.py**:
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', include('django.contrib.auth.urls')),  # Для встроенных форм авторизации
]
```

### 5. Создание шаблонов (templates)

Создадим HTML-шаблоны для страниц регистрации, авторизации, профиля и редактирования профиля.

**users/templates/users/register.html**:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Register</title>
</head>
<body>
    <h2>Register</h2>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Register</button>
    </form>
</body>
</html>
```

**users/templates/users/login.html**:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
</head>
<body>
    <h2>Login</h2>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Login</button>
    </form>
</body>
</html>
```

**users/templates/users/profile.html**:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Profile</title>
</head>
<body>
    <h2>Profile</h2>
    <p>Username: {{ user.username }}</p>
    <p>Email: {{ user.email }}</p>
    <p>Loyalty Points: {{ user.loyalty_points }}</p>
    <p>Referral Code: {{ user.referral_code }}</p>
    <a href="{% url 'edit_profile' %}">Edit Profile</a>
</body>
</html>
```

**users/templates/users/edit_profile.html**:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Edit Profile</title>
</head>
<body>
    <h2>Edit Profile</h2>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Save</button>
    </form>
</body>
</html>
```

### 6. Настройка аутентификации

Добавим настройки аутентификации в **settings.py**:
```python
AUTH_USER_MODEL = 'users.CustomUser'
LOGIN_REDIRECT_URL = 'profile'
LOGOUT_REDIRECT_URL = 'login'
```

### 7. Выполнение миграций

Создадим и применим миграции для базы данных:
```sh
python manage.py makemigrations
python manage.py migrate
```

### 8. Создание суперпользователя

Создадим суперпользователя для доступа к административной панели:
```sh
python manage.py createsuperuser
```
