from ckeditor_uploader.fields import RichTextUploadingField
from categories.models import Categories
from django.db import models



class Product(models.Model):
  # category = models.ManyToManyField(Categories,blank=False,related_name="Categories")
  image = models.ImageField(upload_to="products",blank=True,null=True)
  title = models.CharField(max_length=900,unique=True)
  keyWord = models.TextField(blank=True,null=True,verbose_name='کلمه های کلیدی ')
  about = RichTextUploadingField(blank=True,null=True)
  detail = RichTextUploadingField(blank=True,null=True)
  slug = models.SlugField(max_length=900,blank=False,null=True,unique=True)
  price = models.IntegerField(default=0)
  digital_or_physical = models.BooleanField(default=False,null=True,blank=True,verbose_name=' محصول فیزیکی است ؟ ')
  is_active = models.BooleanField(default=True)
  created = models.DateTimeField(auto_now_add=True)
  ebook = models.FileField(upload_to="fp",blank=True,null=True)

  class Meta:
    verbose_name = 'محصول'
    verbose_name_plural = 'محصولات'

  def __str__(self):
    return f"{self.title}"