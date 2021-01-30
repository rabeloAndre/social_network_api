from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=120)
    phone = models.CharField(max_length=20)
    website = models.CharField(max_length=30)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=80)
    body = models.CharField(max_length=270)
    userId = models.ForeignKey(Profile,
    			related_name='posts',
    			on_delete=models.CASCADE)
    
    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=80)
    email = models.CharField(max_length=50)
    body = models.CharField(max_length=270)
    postId = models.ForeignKey(Post,
                related_name='comments',
                on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name