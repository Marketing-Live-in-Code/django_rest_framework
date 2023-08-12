from django.db import models

# Create your models here.
class Article(models.Model):
    LANGUAGE_CHOICES = [
        ('CH', '中文'),
        ('EG', '英文'),
    ]
    title = models.CharField('標題', max_length=100, null=False)
    language = models.CharField('語言',max_length=2, choices=LANGUAGE_CHOICES, default='', null=False)
    classification_id = models.ForeignKey('Classification', verbose_name='文章分類', on_delete=models.CASCADE)
    number = models.IntegerField('章節課程編號', null=True, blank=True)
    video_url = models.URLField('影片網址', blank=True)
    created_time = models.DateTimeField('保存日期', auto_now = True)
    def __str__(self):
        return self.title
    
class Classification(models.Model):
    title = models.CharField('標題', max_length=100, null=False)
    created_time = models.DateTimeField('保存日期', auto_now = True)
    def __str__(self):
        return self.title