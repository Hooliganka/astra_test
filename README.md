#   Тестовое задание

Запуск:
1. Создаем файл **.env** в корне проекта с таким содержимым
    ```
    DEBUG=1
    SECRET_KEY=cezj7e*ppwu^@=u+@-eg9-a!-%+va@-wed#3v+@5xt5fw$#24x
    DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
    
    POSTGRES_USER=postgres
    POSTGRES_NAME=postgres
    POSTGRES_PASSWORD=postgres
    POSTGRES_HOST=postgres
    POSTGRES_PORT=5432
    ```
2. Далее команда: ```docker-compose build```
3. Запускаем проект: ```docker-compose  up```
4. Переходим по ссылке http://127.0.0.1:8000/