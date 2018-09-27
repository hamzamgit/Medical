from django.db import models
from django.utils import timezone


# Create your models here.

class AppointmentModel(models.Model):
    appointment_name = models.CharField(max_length=50)
    appointment_phone = models.IntegerField()
    appointment_date = models.DateField()
    appointment_message = models.TextField(default='')

    def __str__(self):
        return self.appointment_name


class BannerModel(models.Model):
    banner_title = models.CharField(max_length=255, blank=True)
    banner_detail = models.TextField()
    banner_image = models.ImageField(upload_to='banner/')

    def __str__(self):
        return self.banner_title


class ServicesModel(models.Model):
    service_title = models.CharField(max_length=255, db_column='title')
    service_description = models.TextField(db_column='description')
    service_image = models.ImageField(upload_to='banner/', db_column='image')

    def __str__(self):
        return self.service_title


class ConsultantsModel(models.Model):
    consultant_name = models.CharField(max_length=25)
    consultant_bio = models.CharField(max_length=50)
    consultant_image = models.ImageField(upload_to='consultants/')

    def __str__(self):
        return self.consultant_name


class CommentModel(models.Model):
    comment_username = models.CharField(max_length=25 , db_column='User Name')
    comment_email = models.EmailField( db_column='Email')
    comment_text = models.TextField(db_column='Comment')

    def __str__(self):
        return self.comment_username


class BlogModel(models.Model):
    blog_title = models.CharField(max_length=255)
    blog_content = models.TextField()
    blog_image = models.ImageField()
    blog_comment = models.ManyToManyField(CommentModel)

    def __str__(self):
        return self.blog_title
