Приложение MailingAgent. 
Сервис для управления рассылками.

Инструкция по запуску.
Шаг 1. Клонировать репозиторий.
Шаг 2. Установить зависимости.
Шаг 3. Установить redis и postgresql
Шаг 4. Создать файл .env и внести настройки из .env.sample
    булевы переменные (DEBUG и CACHE_ENABLED): 1 = True else False
    ключ проекта: 'django-insecure-!7&uu^_9^z!!y&!$5srl#kg1nzi(oa^f14g6a4twyw)0i&al6w'
Шаг 5. Применить миграции.
Шаг 6. Создать суперпользователя: 
    python manage.py csu
    # csu_email = 'admin@mail.ru'
    # csu_password = 'admin'
Шаг 7. Создать группы manager и content_manager:
    python manage.py create_mng

    #  в группе manager создается пользователь:
    # email = 'test@test.ru'
    # password = 'test'

    # в группе content_manager создается пользователь:
    # email = 'test1@test.ru'
    # password = 'test1'

Шаг 8. Запустить сервер

