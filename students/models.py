from django.db import models


# Create your models here.

class Students(models.Model):
    @classmethod
    def get_all(cls):
        students =Students.get_all()
    SEX = [
        (1, 'man'),
        (2, 'woman'),
        (0, 'unkonw'),
    ]
    STATUS = [
        (0,'apply'),
        (1,'allow'),
        (2,'reject')
    ]
    name = models.CharField(max_length=128,verbose_name='name')
    sex =models.IntegerField(choices=SEX,verbose_name='sex')
    profession = models.CharField(max_length=128,verbose_name='profession')
    status = models.IntegerField(choices=STATUS,default=0,verbose_name='status')
    email = models.EmailField(verbose_name='email')
    phone = models.CharField(max_length=128,verbose_name='phone')
    creat_time = models.DateTimeField(auto_now_add=True,editable=False,verbose_name='creat_time')
    def __str__(self):
        return '<Student:{}>'.format(self.name)
    class Meta:
        verbose_name = verbose_name_plural = 'students information'

