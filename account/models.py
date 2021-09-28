from django.db import models


class Code(models.Model):
    code = models.CharField(max_length=900,null=True,blank=True,verbose_name='Code')
    phone = models.CharField(max_length=900,null=True,blank=True,verbose_name='Phone')
    status = models.BooleanField(default=False,null=True,blank=True,verbose_name='Status')

    class Meta:
        verbose_name = 'کد'
        verbose_name_plural = 'کد های تایید'


    def __str__(self):
        return f'{self.phone}'
