from django.db import models


class Author(models.Model):
    username = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class Blog(models.Model):
    title = models.CharField(max_length=255, default="")
    blog_text = models.TextField(max_length=500)
    author = models.ForeignKey(
        Author, related_name='writer', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    commentor = models.CharField(max_length=255)
    comment_detail = models.TextField(max_length=200)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment_detail
