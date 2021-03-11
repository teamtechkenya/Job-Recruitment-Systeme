from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone  


class User(AbstractUser):
    is_applicant = models.BooleanField(default=False)
    is_employer = models.BooleanField(default=False)


TYPE_CHOICES = [
    ('FullTime', 'FullTime'),
    ('PartTime', 'PartTime'),
    ('Contract','Contract'),
]

class Jobs(models.Model):
    name = models.CharField(max_length=255)
    jobtype = models.CharField(max_length=15,choices=TYPE_CHOICES)
    employer = models.ForeignKey("Employer", on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    datecreated = models.DateTimeField(editable=False)
    salary = models.IntegerField()
    roles = models.TextField()
    location = models.CharField(max_length=122)
    qualifications = models.TextField()
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.datecreated = timezone.now()
            
    @property
    def no_of_applications(self):
        return Jobs.objects.filter(Jobs=self).count()

class Applicant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    apply = models.ManyToManyField(Jobs)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    address = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    address = models.CharField(max_length=255)
    
    @property
    def employer_jobs(self):
        return Jobs.objects.filter(employer=self)
    
    def __str__(self):
        return self.name
    
class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Jobs, on_delete=models.CASCADE)
    quote = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username