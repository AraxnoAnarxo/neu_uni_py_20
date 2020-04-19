from django.db import models
from datetime import datetime

# Create your models here.

class ActiveManager(models.Manager):
    def get_queryset(self):
        all_objects = super().get_queryset()
        return all_objects.filter(is_active=True)

class IsActiveMixin(models.Model):
    objects = models.Manager()
    active_objects = ActiveManager()
    is_active = models.BooleanField(default=False)
    class Meta:
        abstract = True

class Tag(IsActiveMixin, models.Model):
    tag_name = models.CharField(max_length = 100)

    def __str__(self):
        return f'{self.tag_name}'

class Article(IsActiveMixin,models.Model):
    article_name = models.CharField(max_length = 100, null= True)
    article_text = models.CharField(max_length = 1000, null=True)
    article_date = models.DateTimeField(default=datetime.now())
    article_tag = models.ManyToManyField(Tag)
    article_img = models.ImageField(upload_to = 'articles', null = True, blank = True)
    article_rating = models.IntegerField(default = 0, null=True)

    '''
    DataField - дата
    TimeField - время
    
    Числовые типы:
    IntegerField 
    PositiveIntegerField
    FloatField
    
    Логические типы:
    BooleanField
    
    Байтовый тип:
    BinaryField
    
    Email:
    EmailField
    
    URL:
    URLField
    
    Image:
    ImageField
    
    '''
    def __str__(self):
        return f'{self.article_name}, published: {self.article_date}'



