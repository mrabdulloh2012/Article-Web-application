from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=221)
    description = models.TextField()
    category = models.CharField(max_length=221)
    image = models.ImageField(upload_to='images/')
    author_image = models.ImageField(upload_to='images_author/')
    author_full_name = models.CharField(max_length=221)
    author_position = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Email(models.Model):
    mail = models.EmailField()

    def __str__(self):
        return self.mail
