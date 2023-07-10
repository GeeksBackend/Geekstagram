from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок"
    )
    description = models.CharField(
        max_length=500,
        verbose_name="Описание",
        blank=True, null=True
    )
    image = models.ImageField(
        upload_to='post_images/',
        verbose_name="Фотография",
        blank=True, null=True
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )

    def __str__(self):
        return self.title 
    
    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"