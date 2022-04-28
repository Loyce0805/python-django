from django.db import models

# Create your models here.
class Guest(models.Model):
    # myno = models.AutoField(auto_created = True, primary_key = True)    # ID 따로 생성 X 자동증가 하는 id말고 나만의 ID를 쓸거야
    title = models.CharField(max_length = 50)   # 방명록 제목
    content = models.TextField()     # 방명록 내용 TextField로 더 많은 텍스트 쓸 수 있다.
    regdate = models.DateTimeField()
    
    class Meta:  # Guest class 안에 있는 내부 Class. 더 선호.
        # ordering=('title',)  # title 별로 ascending sort 무조건 tuple이나 list로 해야함. tuple이면 , 찍어줘야함.
        # ordering=('title','id')
        ordering=('-id',)
        
        
        
        
        
        
        