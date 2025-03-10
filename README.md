
# CRUDservice

## Описание
CRUDservice — это современное и функциональное решение для управления данными, обеспечивающее удобный и эффективный способ взаимодействия с базой данных через веб-интерфейс. Проект разработан для автоматизации процессов создания, чтения, обновления и удаления (CRUD) данных, что делает его незаменимым инструментом для управления информацией в различных сферах.

### Требования
- Docker
- Docker Compose

### Установка и запуск

1. Склонируйте репозиторий:
    ```
    git clone https://github.com/axem4n31/CRUDservice.git
    cd CRUDservice
    ```
2. Создайте файл `.env` в корневой директории и добавьте в него переменные окружения, скопировав их из файла `.env.template` или используя предоставленные данные:
    ```
    SECRET_KEY=django-insecure-fqkg(5ed57)ma+k$k&zp=vxtvo18)uo2r+k*^_=a$0k$4z!a)3
    POSTGRES_DB=postgres
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=123123
    POSTGRES_HOST=db
    POSTGRES_PORT=5432
    ```
3. Запустите приложение с помощью Docker::
    ```
    docker-compose up --build
    ```
4. После успешного развёртывания перейдите по адресу http://localhost:8080 для доступа к приложению.

### Использование
- Для взаимодействия с приложением перейдите по адресу http://localhost:8080, где вы сможете тестировать приложение.

### Остановка
Для остановки приложения используйте:
```
docker-compose down
```

### Примечания
- Убедитесь, что порты 8080 (для DRF) и 5432 (для PostgreSQL) не заняты другими приложениями на вашем компьютере.
- Для изменения порта доступа к приложению, отредактируйте файл docker-compose.yml и укажите другой порт в секции ports.

### Контакты
- Автор: Топоров Денис
- Email: toporov.axeman@gmail.com
- Telegram: @axem4n
