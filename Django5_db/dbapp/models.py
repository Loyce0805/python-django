from django.db import models

# Create your models here.  # models.py에서 table 선언
# https://docs.djangoproject.com/en/4.0/topics/db/models/
# CREATE TABLE myapp_person (
#     "id" serial NOT NULL PRIMARY KEY,
#     "first_name" varchar(30) NOT NULL,
#     "last_name" varchar(30) NOT NULL
# );

# from django.db import models   # 위의 sql문을 이렇게 만들어줄 수 있다. id는 pk, auto increment로 자동으로 생성된다.
#
# class Person(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)

class Article(models.Model):
    code = models.CharField(max_length=10)   # Varchar(10) 생각하면 됨.
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    pub_date = models.DateTimeField()
