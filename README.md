# Django Node Modules

[![PyPI version](https://badge.fury.io/py/django-node-modules.svg)](https://badge.fury.io/py/django-node-modules)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/pypi/pyversions/django-node-modules)](https://pypi.org/project/django-node-modules/)
[![Django Version](https://img.shields.io/badge/Django-5.2-green)](https://docs.djangoproject.com/en/5.2/)

**Django Node Modules** — это Django-приложение для удобного управления и обслуживания файлов из локальных `node_modules` и удаленных NPM-пакетов прямо из Django-шаблонов.

## 🚀 Особенности

- **Локальные node_modules**: Автоматическое создание ссылок на файлы из локальных `node_modules`
- **CDN-поддержка**: Подключение файлов напрямую из npm через jsDelivr CDN
- **Безопасность**: Контроль доступа к пакетам через `ALLOWED_NODE_MODULES`
- **Поддержка типов файлов**: JavaScript (модули и обычные), CSS
- **Гибкая настройка**: Рекурсивный поиск, кастомные пути, дополнительные атрибуты

## 📦 Установка

```bash
pip install django-node-modules
```

### Зависимости
- Django 5.2.9
- django-static-engine>=0.1.7, <0.2.0
- filetype>=1.2.0
- requests

## ⚙️ Настройка
1. Добавьте приложение в INSTALLED_APPS:
```python
# settings.py
INSTALLED_APPS = [
    # ...
    'django_node_modules.apps.DjangoNodeModulesConfig',
    # ...
]
```

2. Настройте базовые параметры:
```python
# settings.py
import pathlib

# Обязательная настройка: путь к node_modules
NODE_MODULES_DIR = BASE_DIR / 'node_modules'

# Опционально: список разрешенных пакетов
ALLOWED_NODE_MODULES = ['bootstrap', 'jquery']  # или '__all__' для всех
```

3. Подключите URL:
```python
# urls.py
from django.urls import path, include

urlpatterns = [
    # ...
    path('node_modules/', include('django_node_modules.urls')),
    # ...
]
```

## 📖 Использование
### Шаблонные теги
#### Загрузите теги в шаблон:
```html
{% load node_modules %}
```

### Локальные пакеты
#### JavaScript файлы
```html
{% local_node_js_package "bootstrap" %}
<!-- Или конкретный файл -->
{% local_node_js_package "bootstrap" path="dist/js/bootstrap.min.js" %}

<!-- Как ES-модуль -->
{% local_node_js_package "some-module" path="index.js" module=True %}

<!-- Рекурсивный поиск всех JS файлов -->
{% local_node_js_package "my-package" recursive=True %}
```

#### CSS файлы
```html
{% local_node_css_package "bootstrap" %}
<!-- Или конкретный файл -->
{% local_node_css_package "bootstrap" path="dist/css/bootstrap.min.css" %}
```

### Удаленные пакеты из npm CDN
```html
{% npm_node_package "vue" version="3.4.0" path="dist/vue.global.js" %}
{% npm_node_package "react" path="umd/react.production.min.js" crossorigin="anonymous" %}

<!-- С дополнительными атрибутами -->
{% npm_node_package "jquery" integrity="sha256..." crossorigin="anonymous" defer=True %}
```

## 🔧 Конфигурация
### Настройки приложения


Настройка | Тип | По умолчанию | Описание
-----------------------------------------
`NODE_MODULES_DIR` | `pathlib.Path` | **Обязательно** | Путь к директории `node_modules`
`ALLOWED_NODE_MODULES` | `list` или `str` | `'__all__'` | Список разрешенных пакетов или `__all__`

### Безопасность
По умолчанию доступны все пакеты. Для ограничения доступа:
```python
ALLOWED_NODE_MODULES = [
    'bootstrap',
    'jquery',
    'font-awesome',
    # только эти пакеты будут доступны
]
```

## 🎯 Примеры
### Полный пример шаблона
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Django App</title>
    {% load node_modules %}
    {% local_node_css_package "bootstrap" %}
    {% npm_node_package "font-awesome" path="css/all.min.css" %}
</head>
<body>
    <div id="app">
        <!-- Ваш контент -->
    </div>
    
    {% local_node_js_package "jquery" %}
    {% local_node_js_package "bootstrap" path="dist/js/bootstrap.bundle.min.js" %}
    {% npm_node_package "vue" version="3.4.0" path="dist/vue.global.js" defer=True %}
</body>
</html>
```

### Пример структуры проекта
```text
my_project/
├── node_modules/
│   ├── bootstrap/
│   │   ├── dist/
│   │   │   ├── css/
│   │   │   │   └── bootstrap.min.css
│   │   │   └── js/
│   │   │       └── bootstrap.bundle.min.js
│   │   └── package.json
│   └── jquery/
│       └── dist/
│           └── jquery.min.js
├── my_project/
│   ├── settings.py
│   └── urls.py
└── templates/
    └── base.html
```

## 🔍 API Reference
### Теги шаблонов

`local_node_js_package`
```python
local_node_js_package(package_name: str, 
                      path: Optional[str] = None, 
                      recursive: bool = False, 
                      module: bool = False)
```

`local_node_css_package`
```python
local_node_css_package(package_name: str, 
                       path: Optional[str] = None, 
                       recursive: bool = False)
```

`npm_node_package`
```python
npm_node_package(package_name: str, 
                 version: Optional[str] = None, 
                 path: str = '', 
                 **kwargs)
```

### Утилиты
- `remove_protocol_and_domain()` - Удаляет протокол и домен из URL
- `change_dir()` - Контекстный менеджер для смены директории
- `local_node_file()` - Открывает файл из node_modules

## 🛠 Разработка
### Структура проекта
```text
django_node_modules/
├── templates/
│   └── django_node_modules/
│       ├── local_node_packages.html
│       └── npm_node_packages.html
├── templatetags/
│   ├── __init__.py
│   └── node_modules.py
├── __init__.py
├── apps.py
├── constants.py
├── urls.py
├── utils.py
└── views.py
```

## 🤝 Вклад в разработку
Мы приветствуем вклад в развитие проекта!

1. Форкните репозиторий
2. Создайте ветку для фичи (git checkout -b feature/amazing-feature)
3. Зафиксируйте изменения (git commit -m 'Add amazing feature')
4. Запушьте в ветку (git push origin feature/amazing-feature)
5. Откройте Pull Request

### Отчет об ошибках
Используйте [трекер задач GitHub](https://github.com/magilyasdoma/django-node-modules/issues) для сообщения об ошибках.

## 📄 Лицензия
Распространяется под лицензией MIT. См. файл [`LICENSE`](https://github.com/MagIlyasDOMA/django-node-modules/blob/main/LICENSE) для подробностей.

## 👨‍💻 Автор
Маг Ильяс DOMA (MagIlyasDOMA)

- Email: magilyas.doma.09@list.ru
- GitHub: [@magilyasdoma](https://github.com/magilyasdoma/)

## 🔗 Ссылки
- PyPI: [https://pypi.org/project/django-node-modules/](https://pypi.org/project/django-node-modules/)
- Документация: [https://github.com/magilyasdoma/django-node-modules/blob/main/README.md](https://github.com/magilyasdoma/django-node-modules/blob/main/README.md)
- Исходный код: [https://github.com/magilyasdoma/django-node-modules](https://github.com/magilyasdoma/django-node-modules)
- Трекер задач: [https://github.com/magilyasdoma/django-node-modules/issues](https://github.com/magilyasdoma/django-node-modules/issues)

