from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Post(models.Model):
    whosePost = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    topic = models.CharField(max_length=20, verbose_name='Topic')
    description = models.TextField(verbose_name='Description', max_length=200)
    photo = models.ImageField(verbose_name='Photo', upload_to='posts/media/posts')

    def __str__(self):
        return self.topic

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
    
class Comment(models.Model):
    comment_fk = models.ForeignKey(Post, on_delete=models.CASCADE)
    whose = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(verbose_name='Comment', max_length=200)

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'