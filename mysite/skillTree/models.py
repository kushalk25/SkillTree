from django.db import models

# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500, default='')
    parent_skill = models.ForeignKey('self', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return "{} id={}".format(self.name, self.id)
