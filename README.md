# Flask_Test

## 이 레파지토리는 Flask, SQLAlchemy, Postgresql, Restful API 연결, 통신, 및 사용을 연습해 보기 위함이다.

## 수행되어야 하는 과제 내용:

1. Flask로 서버를 띄우고,
2. Postgresql DB를 하나 생성한 후,
3. machine 테이블을 만들고 port,root_path, max_capacity, left_capacity를 field로 만든다.
4. 라우팅은 Restful API를 사용한다.
5. SQLAlchemy를 이용해서,get, put, post, delete 메서드를 이용한 시나리오들을 수행할수 있게 한다.

> >

    get: 사용자가 port번호를 주면, 그 port에 해당하는 정보를 반환한다.

    put: 사용자가 port번호와 left_capacity를 주면 그 port번호의 left_capacity를 받은 값으로 DB를 업데이트한다.

    post: 사용자가 port번호, root_path, max_capacity, left_capacity를 주면 DB에 그 값을 저장한다.

    delete: 사용자가 port번호를 주면, 해당 port 번호의 정보를 지운다.

## example test 방법:

1. 먼저 install 하고 아래의 run 명령어로 실행한다. 
2. postman을 이용해서 test를 한다. 위에 내용대로 input을 주고, input은 body에 json 형식으로 준다.
3. pgadmin이나 postgres를 실행해서 테이블을 열고 값이 잘 들어왔는지 확인한다.

## RUN 하는 명령어:
>>pip install -r requirements.txt
>>python connect.py

## .env 이런거 필요함
DB_NAME=
DB_USER=
DB_PASS=
DB_SERVICE=localhost
DB_PORT=5432

## 간단한 코드 설명:

.env: 숨겨야 하는 환경변수 저장소

config.py : 환경변수 저장소

connect.py: 메인 코드, 라우팅과 서버 connecting 담당

machine.py : post, get, delete, put의 실제 구현

models.py: 테이블 저장소, db연결

serializer.py: json 반환값을 위해서 필요

## 유용한 레퍼런스들-

### Postgresql

- [Postgresql 설치 및 terminal 이용](https://www.digitalocean.com/community/tutorials/how-to-install-postgresql-on-ubuntu-20-04-quickstart)

- [Pgadmin 설치및 사용법](https://eunsukimme.github.io/database/2019/09/12/Postgresql-Pgadmin/)

> >

    Pgadmin은 테이블을 직접 보고 관리하기 더 쉽게 해주는 프로그램이다.

### SQLAlchemy

- [_SQLAlchemy와 postgresql_](https://www.learndatasci.com/tutorials/using-databases-python-postgres-sqlalchemy-and-alembic/)

- [SQLAlchemy 문법](https://towardsdatascience.com/sqlalchemy-python-tutorial-79a577141a91)

### Flask

- [Flask 설치](https://linuxize.com/post/how-to-install-flask-on-ubuntu-20-04/)

- [Flask_marshmallow](https://www.youtube.com/watch?v=kRNXKzfYrPU)

### Python3

- [convention](ttps://spoqa.github.io/2012/08/03/about-python-coding-convention.html)

> >

    autopep8 extension이 visual studio에 있다.

### Postman(Testing Tool)

- [사용법](https://meetup.toast.com/posts/107)
