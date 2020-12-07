from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.


class Student(models.Model):
    name = models.CharField(verbose_name='NAME', max_length=50)
    number = models.CharField('NUMBER', unique=True, max_length=100, help_text='학번 입력')
    major = models.CharField('MAJOR', max_length=100, blank=False, help_text='전공 입력')
    tel = models.CharField('MOBILE', max_length=50, blank=False)
    email = models.EmailField('EMAIL', max_length=50, blank=True)
    create_dt = models.DateTimeField('CREATE DATE', auto_now_add=True)
    modify_dt = models.DateTimeField('MODIFY DATE', auto_now=True)



    #로그인한 유저의 아이디
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'student'
        verbose_name_plural = 'students'
        ordering = ('-modify_dt',)

    def __str__(self):
        return self.name

