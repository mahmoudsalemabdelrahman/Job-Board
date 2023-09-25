from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.

JOB_TYPE = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),

)

def image_upload(instance, filename):
    imagename, extension = filename.split(".")
    return "jobs/%s/%s.%s"%(instance.id, instance.id,  extension)

class Job(models.Model):
    owner = models.ForeignKey(User, related_name='job_owner' ,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    #location
    job_type = models.CharField(max_length=15, choices= JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField( auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, null=True, blank=True)
    images = models.ImageField(upload_to=image_upload)


    slug = models.SlugField(null=True, blank=True, unique=True)


    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Job,self).save(*args,**kwargs)
   



    def __str__(self):
        return self.title

   



class Category(models.Model):
    name = models.CharField( max_length=30)



    def __str__(self):
        return self.name
    




class Apply(models.Model):
    job = models.ForeignKey(Job, related_name='apply_job', on_delete=models.CASCADE)
    name = models.CharField( max_length=50)
    email = models.EmailField( max_length=254)
    website = models.URLField( max_length=200)
    cv = models.FileField( upload_to='apply/', max_length=100)
    cover_letter = models.TextField(max_length=500)
    created_at = models.DateTimeField( auto_now=True)



    def __dtr__(self):
        return self.name 
   
    

   
