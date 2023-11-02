from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#title
#staus
#date-cureent
#usser
#prioritry

class TODO(models.Model):
    status_choices=[
        ('C','Completed'),
        ('P','Pending')
    ]
    priority_choices=[
        ('1','⓵'),
        ('2','⓶'),
        ('3','⓷'),
        ('4','⓸'),
        ('5','⓹'),
        ('6','⓺'),
        ('7','⓻'),
        ('8','⓼'),
        ('9','⓽'),
        ('10','⓾')
        
    ]
    title=models.CharField(max_length=50)
    status=models.CharField(max_length=2 , choices=status_choices )
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    priority=models.CharField(max_length=2 , choices=priority_choices)
