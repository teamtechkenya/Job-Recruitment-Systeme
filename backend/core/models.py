from django.db import models

#Define abstract user
from django.contrib.auth.models import AbstractUser

from django.db.models.signals import post_save
from django.dispatch import receiver

class CustomUser(AbstractUser):
    user_type_data = ((1, "Employer"), (2, "Applicant"))
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)

class Employer(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

class Applicant(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    gender = models.CharField(max_length=255)
    profile_pic = models.FileField(upload_to='stuent_profile_images ')
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return f'{self.admin.first_name}  {self.admin.last_name} - {self.gender}'

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 1:
            Employer.objects.create(admin=instance)
        
        if instance.user_type == 2:
            Applicant.objects.create(admin=instance,address="",profile_pic="",gender="")

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 1:
        instance.employer.save()
    if instance.user_type == 2:
        instance.applicant.save()