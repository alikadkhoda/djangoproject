from django.db import models

# Create your models here.
class Biography(models.Model):
    class Meta:
        verbose_name = 'بیوگرافی'
        verbose_name_plural = 'بیوگرافی'

    title= models.CharField(max_length=100, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')

    def __str__(self):
        return self.title

class Favorites(models.Model):
    class Meta:
        verbose_name = 'علاقه مندی ها'
        verbose_name_plural = 'علاقه مندی ها'

    title = models.CharField(max_length=100, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')

    def __str__(self):
        return self.title


class Project(models.Model):
    class Meta:
        verbose_name = 'نمونه کارها'
        verbose_name_plural = 'نمونه کارها'

    title = models.CharField(max_length=100, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    project_image = models.ImageField(upload_to='projectImages/', verbose_name='تصویر نمونه کار', null=True, blank=True)

    def __str__(self):
        return self.title