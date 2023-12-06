from django.db import models

# Create your models here.
class model1(models.Model):
    Name=models.CharField(max_length=100)
    Id=models.AutoField(primary_key=True)
    Email=models.EmailField()
    Date_of_birth=models.DateField()
    Age=models.IntegerField()
    Time=models.DateTimeField()
    Joining_Year=models.DecimalField(max_digits=10,decimal_places=3)
    Weight=models.FloatField()
    About_you=models.TextField()
    Your_website_link=models.URLField()
    Upload_your_photo=models.FileField(upload_to='files/')
    Video_duration = models.DurationField()
    Agree=models.BooleanField()