### Создание структуры Django-проекта и необходимых приложений

#### 1. Создание структуры Django-проекта

1. Установим Django и создадим новый проект:
   ```sh
   pip install django
   django-admin startproject istok
   cd istok
   ```

2. Создадим основные приложения:
   ```sh
   python manage.py startapp users
   python manage.py startapp loyalty
   python manage.py startapp orders
   python manage.py startapp products
   python manage.py startapp appointments
   python manage.py startapp chat
   python manage.py startapp promotions
   ```

3. Обновим `settings.py`, добавив созданные приложения:
   ```python
   INSTALLED_APPS = [
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
       'rest_framework',
       'users',
       'loyalty',
       'orders',
       'products',
       'appointments',
       'chat',
       'promotions',
   ]
   ```

#### 2. Определение моделей данных для каждой из функциональных областей

##### Смотрите файл models.md

---

### Дополнительные действия для настройки проекта

#### 1. Настройка `settings.py`

**Основные настройки:**

- **INSTALLED_APPS**: Добавить приложения.
- **DATABASES**: Настроить PostgreSQL.
- **AUTH_USER_MODEL**: Указать кастомную модель пользователя.
- **TEMPLATES**: Убедиться, что шаблоны настроены правильно.
- **STATICFILES**: Настройка статических файлов.
- **MEDIA**: Настройка медиафайлов.

**settings.py**:
```python
import os
from pathlib import Path

# Установим путь к проекту
BASE_DIR = Path(__file__).resolve().parent.parent

# Основные настройки
SECRET_KEY = 'your-secret-key'
DEBUG = True
ALLOWED_HOSTS = []

# Приложения Django
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',         # Ваше приложение users
    'orders',        # Ваше приложение orders
    'products',      # Ваше приложение products
    'appointments',  # Ваше приложение appointments
    'chat',          # Ваше приложение chat
    'promotions',    # Ваше приложение promotions
]

# Мидлвары
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL конфигурация
ROOT_URLCONF = 'istok.urls'

# Шаблоны
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI приложение
WSGI_APPLICATION = 'istok.wsgi.application'

# База данных
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'istok_db',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Пароли
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Интернационализация
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Статические файлы (CSS, JavaScript, изображения)
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Медиа файлы (загружаемые пользователями файлы)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Кастомная модель пользователя
AUTH_USER_MODEL = 'users.CustomUser'

# URL перенаправлений
LOGIN_REDIRECT_URL = 'profile'
LOGOUT_REDIRECT_URL = 'login'

# Почтовая система (для восстановления паролей)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.example.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@example.com'
EMAIL_HOST_PASSWORD = 'your-email-password'
```

#### 2. Настройка PostgreSQL

Если PostgreSQL еще не установлен, его можно установить с помощью следующей команды:

```sh
sudo apt update
sudo apt install postgresql postgresql-contrib
```

#### 3. Создание базы данных и пользователя PostgreSQL

Войдите в командную строку PostgreSQL:

```sh
sudo -u postgres psql
```

Создайте базу данных и пользователя:

```sql
CREATE DATABASE istok_db;
CREATE USER your_db_user WITH PASSWORD 'your_db_password';
ALTER ROLE your_db_user SET client_encoding TO 'utf8';
ALTER ROLE your_db_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE your_db_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE istok_db TO your_db_user;
```

Выйдите из командной строки PostgreSQL:

```sh
\q
```

#### 4. Установка драйвера psycopg2

Для подключения Django к PostgreSQL потребуется драйвер `psycopg2`. Установите его с помощью pip:

```sh
pip install psycopg2-binary
```

#### 5. Применение миграций

Теперь, когда база данных настроена, примените миграции:

```sh
python manage.py makemigrations
python manage.py migrate
```

#### 6. Создание суперпользователя

Создайте суперпользователя для доступа к административной панели Django:

```sh
python manage.py createsuperuser
```

#### 7. Запуск сервера разработки

Запустите сервер разработки, чтобы убедиться, что все настроено правильно:

```sh
python manage.py runserver
```

Теперь ваш проект Django настроен для использования PostgreSQL в качестве базы данных, и основные настройки `settings.py` завершены. Вы можете приступать к разработке и тестированию функциональных модулей.
