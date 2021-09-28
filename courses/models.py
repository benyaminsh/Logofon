from ckeditor_uploader.fields import RichTextUploadingField
from users.models import User
from django.db import models



class Courses(models.Model):
    students = models.IntegerField(default=0,blank=True,null=True,verbose_name='تعداد دانشجویان ')
    CourseLevel = models.CharField(max_length=900,default='مقدماتی',blank=True,null=True,verbose_name='سطح دوره ')
    CourseStatus = models.BooleanField(default=False,blank=True,null=True,verbose_name='آیا دوره  به اتمام رسیده؟ ')
    CourseName = models.CharField(max_length=900,blank=True,null=True,unique=True,verbose_name='نام دوره ')
    CourseDuration = models.CharField(max_length=900,blank=True,null=True,verbose_name='مدت زمان دوره : 45:25:00 ')
    CourseSlug = models.SlugField(max_length=900,blank=True,null=True,verbose_name='آدرس url ')
    CoursePrice = models.IntegerField(default=0,blank=True,null=True,verbose_name='قیمت دوره ')
    CourseStatus = models.BooleanField(default=False,blank=True,null=True,verbose_name='وضعیت نمایش ')
    CourseImage = models.ImageField(upload_to='CourseImage',blank=True,null=True,verbose_name='تصویر دوره ')
    keyWord = models.TextField(blank=True,null=True,verbose_name='کلمه های کلیدی ')
    CourseDescription = RichTextUploadingField(blank=True,null=True,verbose_name='توضیحات دوره ')

    class Meta:
        verbose_name = 'دوره'
        verbose_name_plural = 'دوره ها'

    def __str__(self):
        return f'{self.CourseName}'




class Students(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='دانشجو ')
    course = models.ForeignKey(Courses,on_delete=models.CASCADE,verbose_name='دوره ',related_name='Students_set')

    def __str__(self):
        return f'{self.owner} - {self.course}'

    class Meta:
        verbose_name = 'دانشجو'
        verbose_name_plural = 'دانشجو ها'

    




class Videos(models.Model):
    title = models.CharField(max_length=999,blank=True,null=True,verbose_name=' عنوان ویدیو')
    video = models.FileField(upload_to='Courses/Videos/',blank=True,null=True,verbose_name=' ویدیو')
    course = models.ForeignKey(Courses,on_delete=models.CASCADE,blank=True,null=True,verbose_name=' دوره',related_name='videos_set')


    def __str__(self):
        return f'ویدیو   : {self.title} - {self.course}'

    class Meta:
        verbose_name = 'ویدیو'
        verbose_name_plural = 'ویدیو ها'


class IntroductionVideo(models.Model):
    video = models.FileField(upload_to='Courses/IntroductionVideo/',blank=True,null=True,verbose_name='  ویدیو معرفی')
    course = models.ForeignKey(Courses,on_delete=models.CASCADE,blank=True,null=True,verbose_name=' دوره',related_name='IntroductionVideo_set')

    def __str__(self):
        return f'ویدیو معرفی دوره : {self.course.CourseName}'

    class Meta:
        verbose_name = 'ویدیو'
        verbose_name_plural = 'ویدیو های معرفی'

