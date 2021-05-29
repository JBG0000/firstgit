from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 200)  #제한 글자 200자, 문자
    writer = models.CharField(max_length=100)   #제한 글자 100자, 문자
    pub_date = models.DateTimeField()           #날짜와 시간을 저장해주는 Field 사용
    body = models.TextField()                   #본문은 글자수 제한이 없는 Text 필드 사용
    image = models.ImageField(upload_to="blog/",blank=True, null=True)     #이미지 입력받을땐 image필드 사용 : upload_to는 업로드한 폴더 지정하는 용도, 사진 업로드 하지 않을 시 에러방지 블랭크, 널

    def __str__(self):  #어디서 객체가 호출되었을 때 나타나는 이름표
        return self.title   #객체 호출시 클래스 중 title로 이름이 나타나도록 설정

    def summary(self):
        return self.body[:100]  #본문 body가 100자를 넘어갈경우 100자까지만 슬래싱하여 출력