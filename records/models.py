from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Category:
    Name = (
        ('Python', 'Python'),
        ('JavaScript', 'JavaScript'),
        ('Linux', 'Linux'),
        ('Django', 'Django'),
        ('Java', 'Java'),
        ('ML', 'ML')
    )


# Create your models here.
class Team(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    photo = models.ImageField(null=False, blank=False, upload_to='media/')
    member_about = models.CharField(max_length=40, null=True, blank=True)

    def __str__(self):
        return str(self.name)


class Details(models.Model):
    about = models.CharField(max_length=200, null=False, blank=False)
    contact = models.CharField(max_length=20, blank=False)
    email = models.EmailField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.contact


class BlogCategory(models.Model):
    name = models.CharField(max_length=20, choices=Category.Name, blank=False, null=False)
    description = models.CharField(max_length=200, blank=False, null=False)
    blog_photo = models.ImageField(blank=False, null=False, upload_to='media/')

    def __str__(self):
        return self.name


class BlogDetails(models.Model):
    technology = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, null=False, blank=False)
    short_details = models.CharField(max_length=40, null=False, blank=False)
    description = RichTextField(null=False, blank=False)
    blog_details_photo = models.ImageField(null=True, blank=True, upload_to='media/')
    written_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    comments = models.TextField()

    def __str__(self):
        return self.short_details
