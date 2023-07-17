from django.contrib import admin

from apps.posts.models import Post, PostLike, PostComment

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'description', 'created')

@admin.register(PostLike)
class PostLikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'post')

@admin.register(PostComment)
class PostCommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'text', 'created')
    search_fields = ('user__username', 'post__title', 'text')