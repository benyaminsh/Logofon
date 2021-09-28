from django.db import models

class Categories(models.Model):
    title = models.CharField(max_length=900,blank=True,null=True,verbose_name='Categorie Name')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


    def __str__(self):
        return f'{self.title}'