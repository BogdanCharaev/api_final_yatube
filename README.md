# api_final
api сайта Yatube

Позволяет обращаться к моделям Post, Comment, Follows и Group 
сайта Yatube

Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:

git clone https://github.com/yandex-praktikum/kittygram2.git
cd kittygram2
Cоздать и активировать виртуальное окружение:

python3 -m venv env
source env/bin/activate
python3 -m pip install --upgrade pip
Установить зависимости из файла requirements.txt:

pip install -r requirements.txt
Выполнить миграции:

python3 manage.py migrate
Запустить проект:

python3 manage.py runserver

Примеры запросов:

- GET /api/v1/posts:

Response:

{
"count": 123,
"next": "http://api.example.org/accounts/?offset=400&limit=100",
"previous": "http://api.example.org/accounts/?offset=200&limit=100",
"results": [
{
"id": 0,
"author": "string",
"text": "string",
"pub_date": "2021-10-14T20:41:29.648Z",
"image": "string",
"group": 0
}
]
}

- POST /api/v1/posts 

{
"text": "string",
"image": "string",
"group": 0
}

Response:

{
"id": 0,
"author": "string",
"text": "string",
"pub_date": "2019-08-24T14:15:22Z",
"image": "string",
"group": 0
}

GET /api/v1/posts/{id}:

Response:

{
"id": 0,
"author": "string",
"text": "string",
"pub_date": "2019-08-24T14:15:22Z",
"image": "string",
"group": 0
}
