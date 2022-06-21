from django.contrib.auth.models import User
from django.db import models


class Problem(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    img = models.ImageField(upload_to='IMG-PROBLEM')
    code = models.FileField(upload_to='code')

    class Meta:
        db_table = 'problem'

    def __str__(self) -> object:
        return self.title
