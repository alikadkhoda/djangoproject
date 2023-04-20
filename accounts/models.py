from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class ProfileModel(models.Model):
    class Meta:
        verbose_name= "کاربر"
        verbose_name_plural= "کاربرها"


    user=models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="کاربری", related_name="profile")
    ProfileImage= models.ImageField(upload_to="ProfileImage/", verbose_name="عکس")
    birthday=models.DateField(verbose_name="تاریخ تولد")


    def __str__(self):
        return self.user.username



