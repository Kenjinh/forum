from django.db import models
from users.models import User

# Create your models here.

class PostCategory(models.Model):
    category: str = models.CharField(max_length=50)

    class Meta:
        db_table = 'tb_forum_topics_posts_ctg'


class Post(models.Model):
    category = models.ForeignKey(PostCategory, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    publish_date = models.DateField(auto_created=True)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images/')

    class Meta:
        db_table = 'tb_forum_topics_posts'


class Comment(models.Model):
    post: int = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    publish_date = models.DateField(auto_created=True)
    comment: str = models.CharField(max_length=500)

    class Meta:
        db_table = 'tb_forum_topics_comments'

