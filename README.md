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
- **Специальная поддержка hrenpack пакетов**: Упрощенное подключение hrenpack_js и hrenpack-theme-style
- **Кеширование конфигураций**: Оптимизация загрузки конфигов популярных пакетов

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

# Опционально: кеширование конфига hrenpack-theme-style (по умолчанию True)
CACHE_HRENPACK_THEME_STYLE_CONFIG = True
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
<!-- Для стандартных пакетов -->
{% load node_modules %}

<!-- Для hrenpack пакетов -->
{% load node_hrenpack %}
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

## 🔧 Специальная поддержка hrenpack пакетов
### hrenpack_js
`hrenpack_js` — это пакет с набором полезных JavaScript утилит и компонентов.

#### Подключение CSS
```html
{% hrenpack_js_css %}
<!-- С указанием версии -->
{% hrenpack_js_css version="1.2.0" %}
```

#### Подключение JavaScript
```html
<!-- Все скрипты -->
{% hrenpack_js_scripts "all" %}

<!-- Или -->
{% hrenpack_js_scripts %}

<!-- Только указанные скрипты -->
{% hrenpack_js_scripts "include" "utils.js" "components.js" %}

<!-- Все, кроме указанных -->
{% hrenpack_js_scripts "exclude" "deprecated.js" %}

<!-- С указанием версии -->
{% hrenpack_js_scripts "all" version="1.2.0" %}
```

### hrenpack-theme-style
`hrenpack-theme-style` — это пакет с темами и стилями для интерфейсов.

#### Подключение CSS
```html
{% hrenpack_theme_style_css %}
```

#### Подключение JavaScript
```html
<!-- Базовая конфигурация (только основной скрипт) -->
{% hrenpack_theme_style_css "base" %}

<!-- Поддержка темной темы -->
{% hrenpack_theme_style_css "dark_theme" %}

<!-- Стили для форм -->
{% hrenpack_theme_style_css "form" %}

<!-- Полная конфигурация (все стили) -->
{% hrenpack_theme_style_css "full" %}

<!-- Или -->
{% hrenpack_theme_style_css %}
```
**Примечание:** JavaScript темы по умолчанию включают необходимые зависимости из hrenpack_js, если не указан параметр no_deps=True.

### Автоматическое определение источника
Пакет автоматически определяет, использовать ли локальную версию или CDN:

- Если пакет существует локально в node_modules и не указана версия → используется локальная версия
- В противном случае → используется CDN версия

## 🔧 Конфигурация
### Настройки приложения

|              Настройка              |       Тип        |  По умолчанию   | Описание                                  |
|:-----------------------------------:|:----------------:|:---------------:|:-----------------------------------------:|
|         `NODE_MODULES_DIR`          |  `pathlib.Path`  | **Обязательно** | Путь к директории `node_modules`          |
|       `ALLOWED_NODE_MODULES`        | `list` или `str` |   `'__all__'`   | Список разрешенных пакетов или `__all__`  |
| `CACHE_HRENPACK_THEME_STYLE_CONFIG` |      `bool`      |     `True`      | Кешировать ли конфиг hrenpack-theme-style |

### Безопасность
По умолчанию доступны все пакеты. Для ограничения доступа:
```python
ALLOWED_NODE_MODULES = [
    'bootstrap',
    'jquery',
    'font-awesome',
    'hrenpack_js',
    'hrenpack-theme-style',
    # только эти пакеты будут доступны
]
```

## 🎯 Примеры
### Полный пример шаблона с hrenpack
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Django App with hrenpack</title>
    
    {% load node_modules %}
    {% load node_hrenpack %}
    
    <!-- Стандартные пакеты -->
    {% local_node_css_package "bootstrap" %}
    
    <!-- hrenpack темы -->
    {% hrenpack_theme_style_css "light" %}
    
    <!-- CSS для hrenpack_js -->
    {% hrenpack_js_css %}
</head>
<body class="hrenpack-light-theme">
    <div id="app">
        <!-- Ваш контент -->
    </div>
    
    <!-- Стандартные пакеты -->
    {% local_node_js_package "jquery" %}
    {% local_node_js_package "bootstrap" path="dist/js/bootstrap.bundle.min.js" %}
    
    <!-- hrenpack JavaScript -->
    {% hrenpack_theme_style_scripts "light" %}
    {% hrenpack_js_scripts "include" "utils.js" "components.js" %}
    
    <!-- Vue.js из CDN -->
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
│   ├── hrenpack_js/
│   │   ├── index.js
│   │   ├── utils.js
│   │   ├── components.js
│   │   ├── styles.css
│   │   └── package.json
│   └── hrenpack-theme-style/
│       ├── light/
│       │   ├── theme.css
│       │   └── theme.js
│       ├── dark/
│       │   ├── theme.css
│       │   └── theme.js
│       └── package.json
├── my_project/
│   ├── settings.py
│   └── urls.py
└── templates/
    └── base.html
```

## 🔍 API Reference
### Стандартные теги шаблонов

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

### hrenpack теги шаблонов
`hrenpack_js_css`
```python
hrenpack_js_css(version: Optional[str] = None)
```

`hrenpack_js_scripts`
```python
hrenpack_js_scripts(type: Literal['include', 'exclude', 'all'] = 'all', 
                    *args, 
                    version: Optional[str] = None)
```

`hrenpack_theme_style_css`
```python
hrenpack_theme_style_css(config: str = 'full', 
                         version: Optional[str] = None)
```

`hrenpack_theme_style_scripts`
```python
hrenpack_theme_style_scripts(config: str = 'full', 
                            version: Optional[str] = None, 
                            no_deps: bool = False)
```

## 🛠 Разработка
### Структура проекта
```text
django_node_modules/
├── templates/
│   └── django_node_modules/
│       ├── local_node_packages.html
│       ├── npm_node_packages.html
│       └── hrenpack/
│           ├── css.html
│           ├── hrenpack-theme-style.html
│           └── hrenpack_js.html
├── templatetags/
│   ├── __init__.py
│   ├── node_modules.py        # Стандартные теги
│   └── node_hrenpack.py       # hrenpack теги
├── __init__.py
├── apps.py
├── constants.py
├── urls.py
├── utils/                     # Утилиты
│   ├── __init__.py
│   ├── base.py
│   ├── hrenpack_base.py
│   ├── hrenpack_js.py
│   └── hrenpack_theme_style.py
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
- hrenpack-theme-style конфиг: [https://raw.githubusercontent.com/magilyasdoma/hrenpack-theme-style/main/config-api.json](https://raw.githubusercontent.com/magilyasdoma/hrenpack-theme-style/main/config-api.json)
