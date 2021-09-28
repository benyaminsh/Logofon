from django.db import models



class ContactUs(models.Model):
    name = models.CharField(max_length=900,blank=True,null=True,verbose_name='Name')
    email = models.CharField(max_length=900,blank=True,null=True,verbose_name='Email')
    subject = models.CharField(max_length=900,blank=True,null=True,verbose_name='Subject')
    message = models.TextField(blank=True,null=True,verbose_name='message')
    status = models.BooleanField(default=False,blank=True,null=True,verbose_name='Status')

    class Meta:
        verbose_name = 'تنظیمات'
        verbose_name_plural = 'تماس با ما'


    def __str__(self):
        return f'{self.name}'



