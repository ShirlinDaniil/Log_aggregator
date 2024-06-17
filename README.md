# Log Aggregator

## Описание

Log Aggregator — это приложение на Django, которое собирает и агрегирует данные из access логов веб-сервера Apache.
 Оно позволяет просматривать сохраненные данные, фильтровать их по IP, дате и временным промежуткам, а также предоставляет API для получения данных в формате JSON.

## Требования

- Python 3.9+
- Django 3.2+
- PostgreSQL
- `psycopg2-binary`
- `pytz`

## Установка

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/ShirlinDaniil/Log_aggregator.git
   cd Log_aggregator

2. Создайте и активируйте виртуальное окружение:
  python3 -m venv venv
source venv/bin/activate

3. Установите зависимости:
pip install -r requirements.txt

4. Настройте базу данных в log_aggregator/settings.py:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'log_aggregator_db',
        'USER': 'log_user',
        'PASSWORD': 'your_password', # Установите свой пароль
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

5. Примените миграции:

python manage.py makemigrations
python manage.py migrate

6. Создайте суперпользователя для доступа к админке:

python manage.py createsuperuser


## Использование
Парсинг логов
Для парсинга логов Apache запустите команду:

python manage.py parse_logs

Просмотр данных
Вы можете просматривать данные через консольные команды. Примеры:

python manage.py view_logs 2024-06-01
python manage.py view_logs 2024-06-01 2024-06-10 ip
python manage.py view_logs 2024-06-01 2024-06-10 status

Запуск сервера
Для запуска сервера разработки выполните:

python manage.py runserver

Перейдите по адресу http://127.0.0.1:8000/admin/ для доступа к админке и по адресу http://127.0.0.1:8000/api/logs/ для доступа к API.

Настройка cron
Для автоматического парсинга логов каждый день в полночь добавьте задание в crontab:

crontab -e

Добавьте следующую строку:

0 0 * * * {Указать верный путь}/PycharmProjects/Log_aggregator/.venv/bin/python /Users/{Указать пользователя}/PycharmProjects/Log_aggregator/manage.py parse_logs
