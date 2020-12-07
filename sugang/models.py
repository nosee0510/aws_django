from django.db import models
from django.urls import reverse


class Subject(models.Model):
    name = models.CharField('NAME', max_length=30)
    description = models.CharField('One Line Description', max_length=100, blank=True)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='OWNER', blank=True, null=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('sugang:subject_detail', args=(self.id,))


class Apply(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    name = models.CharField('NAME', max_length=20)
    number = models.CharField('NUMBER', max_length=20)
    major = models.CharField('MAJOR', max_length=20) #upload_to 이미지가 저장될 폴더
    upload_dt = models.DateTimeField('UPDATE DATE', auto_now_add=True)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='OWNER', blank=True, null=True)  # 추가①

    class Meta:
        ordering = ('subject',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('sugang:apply_detail', args=(self.id,))