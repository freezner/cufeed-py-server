from django.db import models

# Create your models here.
class Feeds(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255, help_text="수집된 뉴스의 제목")
    link = models.CharField(max_length=1000, help_text="수집된 뉴스의 하이퍼링크")
    link_hash = models.CharField(max_length=100, help_text="수집된 뉴스의 고유 해시값")
    keyword = models.CharField(max_length=100, help_text="수집에 사용된 키워드")
    vendor = models.CharField(max_length=20, help_text="뉴스 정보의 제공자 정보")
    create_date = models.DateTimeField(auto_now_add=True, help_text="뉴스 수집 일시")
    update_date = models.DateTimeField(auto_now=True, help_text="뉴스 수집 정보 변경 일시")


class RegisterQueues(models.Model):
    id = models.BigAutoField(primary_key=True)
    keyword = models.CharField(max_length=255, help_text="수집 요청 키워드")
    status = models.CharField(max_length=20, help_text="상태 - 요청: requested, 처리중: processing, 완료: completed, 실패: failed")
    create_date = models.DateTimeField(auto_now_add=True, help_text="수집 요청 일시")
    update_date = models.DateTimeField(auto_now=True, help_text="수집 요청 변경 일시")
