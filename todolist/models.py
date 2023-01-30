from django.db import models
from django.urls import reverse
class Todolist(models.Model):
    todo_title = models.CharField(max_length=30)
    todo_url = models.URLField(blank=True)
    todo_priority = models.IntegerField('우선 순위 입력',default=0,help_text='우선 순위는 0~9사이로 입력하세요.')
    todo_completion = models.IntegerField('완료 여부 입력',default=0,help_text='완료 여부는 0과 1로 입력하세요.')
    category = models.ManyToManyField('Category')
    
   

    def __str__(self):
        return self.todo_title


class Category(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


  



