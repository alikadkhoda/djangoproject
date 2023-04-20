from django.db import models

# Create your models here.
class Conference(models.Model):
    class Meta:
        verbose_name ='کنفرانس'
        verbose_name_plural ='کنفرانس ها'

    TOPIC_CHOICES = [
        ('0', 'مهندسی و علوم فیزیکی'),
        ('1', 'کشاورزی و علوم زیستی'),
        ('2', 'پزشکی'),
        ('3', 'علوم انسانی'),
    ]

    TYPE_CHOICES = [
        ('0', 'منطقه ای'),
        ('1', 'ملی'),
        ('2', 'بین المللی'),
    ]
    confTopic = models.CharField(max_length=1, choices=TOPIC_CHOICES, verbose_name='موضوع کنفرانس')
    confType = models.CharField(max_length=500, choices=TYPE_CHOICES, verbose_name='نوع کنفرانس')
    title = models.CharField(max_length=500, verbose_name='عنوان کنفرانس')
    event_date = models.DateField(verbose_name='تاریخ برگزاری')
    event_place = models.CharField(max_length=500, verbose_name='محل برگزاری')

    def __str__(self):
        return self.title


class Journal(models.Model):
    class Meta:
        verbose_name ='ژورنال'
        verbose_name_plural ='ژورنال ها'
    CHOICES = [
        ('0', 'داخلی'),
        ('1', 'خارجی'),
               ]
    journalType = models.CharField(max_length=1, choices=CHOICES, verbose_name='نوع ژورنال')
    title = models.CharField(max_length=500, verbose_name='عنوان ژورنال')
    issn = models.CharField(max_length=500, verbose_name='شابک')
    volume = models.CharField(max_length=500, verbose_name='شمارگان ژورنال')
    publisher = models.CharField(max_length=500, verbose_name='ناشر')
    rank = models.CharField(max_length=500, verbose_name='رتبه ژورنال')

    def __str__(self):
        return self.title


class Paper(models.Model):
    class Meta:
        verbose_name ='مقاله'
        verbose_name_plural ='مقاله ها'
    CHOICES = [
        ('0', 'ژورنال داخلی'),
        ('1', 'ژورنال خارجی'),
        ('2', 'کنفرانس داخلی'),
        ('3', 'کنفرانس خارجی'),
               ]
    paperType = models.CharField(max_length=1, choices=CHOICES, verbose_name='نوع مقاله')
    title = models.CharField(max_length=500, verbose_name='عنوان مقاله')
    doi = models.CharField(max_length=1000)
    author1 = models.CharField(max_length=500, verbose_name='نویسنده اول')
    author2 = models.CharField(max_length=500, verbose_name='نویسنده دوم')
    author3 = models.CharField(max_length=500, verbose_name='نویسنده سوم')
    author4 = models.CharField(max_length=500, verbose_name='نویسنده چهارم')
    abstract = models.TextField(verbose_name='چکیده مقاله')
    volume = models.CharField(max_length=500, verbose_name='شمارگان ژورنال')
    publication_date = models.DateField(verbose_name='تاریخ انتشار')
    paper_image = models.ImageField(upload_to='paperImages/', verbose_name='تصویر مقاله', null=True, blank=True)
    pdfjournal = models.FileField(upload_to='pdf/', verbose_name='pdf مقاله', null=True, blank=True)
    conference = models.ForeignKey(Conference, on_delete=models.PROTECT, null=True, verbose_name='کنفرانس', blank=True)
    journal = models.ForeignKey(Journal, on_delete=models.PROTECT, null=True, verbose_name='ژورنال', blank=True)

    def __str__(self):
        return self.title


class Jozveh(models.Model):
    class Meta:
        verbose_name = 'جزوه ها'
        verbose_name_plural = 'جزوه ها'

    title = models.CharField(max_length=200, verbose_name='عنوان')
    prof = models.CharField(max_length=150, verbose_name='نام استاد')
    pdfjozveh = models.FileField(upload_to='pdfjozveh/', verbose_name='pdf جزوه', null=True, blank=True)
    jozveh_image = models.ImageField(upload_to='jozvehImages/', verbose_name='تصویر جزوه', null=True, blank=True)

    def __str__(self):
        return self.title


class Presentation(models.Model):
    class Meta:
        verbose_name = 'ارائه ها'
        verbose_name_plural = 'ارائه ها'

    title = models.CharField(max_length=200, verbose_name='عنوان')
    pdfpresentation = models.FileField(upload_to='pdfPresentation/', verbose_name='pdf ارائه', null=True, blank=True)
    presentation_image = models.ImageField(upload_to='presentationImages/', verbose_name='تصویر ارائه', null=True, blank=True)

    def __str__(self):
        return self.title