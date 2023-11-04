## "Образовательные модули"

Проект на Django и Django Rest Framework, включает в себя два приложения "Модули" и "Пользователи"

### Запуск проекта в Docker:
Необходимо создать файл docker.env и заполнить его по образцу docker.env.sample, а также файл .env заполнить по образцу .env.sample


`docker-compose up -d --build` - создание образов и запуск контейнера


`docker-compose up -d --build` - остановка контейнера


Модель "Модули" содержит следующие поля:
- номер,
- название,
- описание,
- пользователь создавший модуль


Настроена авторизация пользователя с помощью JWT. <br>
При регистрации пользователю необходимо указать email, пароль, имя, фамилию (опционально номер телефона и дату рождения).
Если пользователь указывает дату рождения, то ему в день рождения приходит на почту поздравление.


#### Права доступа:
 - Новые модули может создавать любой авторизированный пользователь
 - Просматривать общий список модулей могут любые пользователи (в том числе и неавторизованные), но для детального просмотра необходима авторизация
 - Редактировать и удалять пользователь может только созданные им модули
 - Просмотр, редактирование и удаление пользователя доступно только для админов.


#### Документация:
http://localhost:8000/swagger/ <br>
или <br>
http://localhost:8000/redoc/


Для всех моделей, сериализаторов и вьюс написаны юнит-тесты<br>


В проекте присутствует механизм безопасности CORS.

Для запуска периодической задачи отправки поздравлений:
`celery -A config worker -l INFO` <br>
`celery -A config beat -l INFO -S django` 
<hr>

## Стек:
- Python 3.11
- Docker
- Django
- DRF
- Swagger
- PostgreSQL
- JWT
- Celery
- Redis
- CORS
- Unittest
- Flake8
