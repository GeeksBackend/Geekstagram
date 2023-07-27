from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='user_posts',
        verbose_name="Пользователь"
    )
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

class PostLike(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL,
        related_name='users_likes',
        verbose_name='Пользователь',
        null=True
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE,
        related_name='post_likes',
        verbose_name='Пост'
    )

    def __str__(self):
        return f"{self.user} {self.post}"

    class Meta:
        verbose_name = "Лайк" 
        verbose_name_plural = "Лайки"

class PostComment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='user_comments',
        verbose_name='Пользователь'
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE,
        related_name='post_comments',
        verbose_name='Пост'
    )
    text = models.CharField(
        max_length=300,
        verbose_name='Текст комментария'
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )

    def __str__(self):
        return f"{self.user} {self.post}"

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

class PostFavorite(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='user_favorites',
        verbose_name="Пользователь"
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE,
        related_name='favorite_users',
        verbose_name="Пост"
    )

    def __str__(self):
        return f"{self.user} {self.post}"

    class Meta:
        verbose_name = "Избранное"
        verbose_name_plural = "Избранные"