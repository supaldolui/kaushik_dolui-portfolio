from django.db import models
from cloudinary.models import CloudinaryField
class Level(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class SkillCard(models.Model):
    title = models.CharField(max_length=255)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    image = CloudinaryField('skill_images')

    def __str__(self):
        return self.title

class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name 
    
class ProjectCard(models.Model):
    title = models.CharField(max_length=255)
    languages = models.CharField(max_length=255)
    image = CloudinaryField('project_images')
    

    def __str__(self):
        return self.title
    
