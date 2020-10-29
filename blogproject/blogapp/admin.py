from django.contrib import admin
from .models import Post, Comment, Category

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_full_name', 'post_date', 'category', 'nr_comments', 'likes', 'visible']
    search_fields = ['title', 'category__name', 'author__first_name']
    def get_full_name(self, instance):
        return instance.author.first_name + ' ' + instance.author.last_name
    def nr_comments(self, instance):
        return Comment.objects.filter(post=instance).count()
    get_full_name.short_description = 'Author Name'
    nr_comments.short_description = 'Number of Comments'
    class Media:
        js = ('js/post.js',)

admin.site.register(Post, PostAdmin)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'post', 'comment_date', 'visible']
    search_fields = ['author', 'post__title']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_nr_posts', 'nr_comments', 'nr_likes']
    def get_nr_posts(self, instance):
        return Post.objects.filter(category=instance).count()
    def nr_comments(self, instance):
        return Comment.objects.filter(post__category=instance).count()
    def nr_likes(self, instance):
        posts = Post.objects.filter(category=instance, likes__gt=0)
        total_likes = 0
        for post in posts:
            total_likes += post.likes
        return total_likes
    get_nr_posts.short_description = 'Number of Posts'
    nr_comments.short_description = 'Total Comments'
    nr_likes.short_description = 'Total Likes'