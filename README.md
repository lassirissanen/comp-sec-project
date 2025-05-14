# comp-sec-project
Course project for secure programming course. The application is a simple web forum where users can register, login, make posts and comment on other posts.

# Requirements
- python 3.10
- docker

# Usage

Copy the example .env files to `.env.local` and `.env.prod`

## local

install dependencies:

``` shell
pip install -r requirements.txt
```

Go to project directory:
``` shell
cd project
```

Run database migrations
``` shell
py manage.py migrate
```

Run the application:
``` shell
py manage.py runserver
```

The app will be accessible at port 8000

## "production" with docker compose

Run:
``` shell
docker compose up -d --build
```

The app will be accessible at port 8001
