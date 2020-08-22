from django.db import models

# Create your models here.


class Article(models.Model):
    class Meta:
        ordering = ["-created"]

    title = models.CharField(verbose_name="Заголовок", max_length=255)
    text = models.TextField(verbose_name="Текст")

    image = models.ImageField(upload_to='images/')

    created = models.DateTimeField(auto_now_add=True)
