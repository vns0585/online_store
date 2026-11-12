# Интернет-магазин

## Описание проекта

Проект представляет собой интернет-магазин, реализованный на фреймворке Django. На текущем этапе реализованы базовая структура проекта, приложение catalog, главная страница и страница контактов с формой обратной связи.

##  Стек технологий

- Python 3.14
- Poetry 2.4.1 - инструмент для управления зависимостями 
- Django 6.1.3 - веб-фреймворк
- Bootstrap 5.3.8 - CSS-фреймворк для стилизации

## Установка и запуск

###  Клонирование репозитория
```bash
git clone https://github.com/vns0585/online_store.git
cd <каталог проекта>
```

### Установка Poetry
Если Poetry ещё не установлен:
#### macOS / Linux:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```
#### Windows (PowerShell):
```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```
Проверка установки:
```bash
poetry --version
```

### Установка зависимостей
```bash
poetry install
```

### Сгенерируйте SECRET_KEY для Djando
Выполните одну команду и скопируйте результат в переменную SECRET_KEY
в файле <путь_к_пректу>/config/.env
```bash
poetry run python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```
Пример полученного ключа:
```text
django-insecure-3k$9f!x#2v@8m&q1p^7n*r4t+u6w=y0z(l)o_b%c5h.a7s-d9f
```
Скопируйте его в <путь_к_пректу>/config/.env:
```dotenv
SECRET_KEY=django-insecure-3k$9f!x#2v@8m&q1p^7n*r4t+u6w=y0z(l)o_b%c5h.a7s-d9f
```

***Важно***: файл .env содержит секреты и не должен попадать в git. Убедитесь, что он добавлен в .gitignore.

### Активация виртуального окружения
```bash
poetry shell
```
#### Альтернатива без активации — запускать команды через poetry run:
```bash
poetry run python manage.py runserver
```

### Применение миграций
```bash
poetry run python manage.py migrate
```

### Запуск сервера разработки
```bash
poetry run python manage.py runserver
```
После запуска проект будет доступен по адресу: http://127.0.0.1:8000/

## Структура проекта
```text
online_store/
├── config/                 # Основные настройки Django-проекта
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── catalog/                # Приложение каталога
│   ├── templates/
│   │   └── catalog/
│   │       ├── home.html
│   │       └── contacts.html
│   ├── views.py
│   ├── urls.py
│   └── ...
├── manage.py
├── pyproject.toml          # Зависимости и настройки Poetry
├── poetry.lock             # Зафиксированные версии зависимостей
├── .gitignore
└── README.md
```

## Лицензия
Этот проект лицензирован по [лицензии MIT](LICENSE).