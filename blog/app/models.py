from django.db import models

class New(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='image_new')
    description = models.TextField()
    full_text = models.TextField()
    date_time = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title


class User(models.Model):
    login = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.login


class Comment(models.Model):
    text = models.TextField()
    name = models.TextField()
    new = models.ForeignKey(New, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)