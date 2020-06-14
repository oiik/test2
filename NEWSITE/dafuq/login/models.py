from django.db import models

# Create your models here.


#class MyGroups(models.Model):
    #name = models.CharField(max_length=10, null=True)
    #users =

class Course(models.Model):
    TIMES = (('8.30-10.00','8.30-10.00'),
    ('10.10-11.40','10.10-11.40'),
    ('11.50-13.20','11.50-13.20'),
    )

    name = models.CharField(max_length=200, null=True)
    teacher = models.CharField(max_length=150, null=True)
    room = models.CharField(max_length=50, null=True)
    time = models.CharField(max_length=30, null = True, choices=TIMES)
    #group = models.ForeignKey(MyGroups, null=True, on_delete=models.SET_NULL)


    def __str__(self):
        return self.name
