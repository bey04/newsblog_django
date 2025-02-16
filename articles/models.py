from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from taggit.managers import TaggableManager
from ckeditor_uploader.fields import RichTextUploadingField

class Article(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField(max_length=500, blank=True)
    body = RichTextUploadingField()
    image = models.ImageField(upload_to='images/', blank=True)
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(), 
        on_delete=models.CASCADE,
    )
    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    comment = models.CharField(max_length=150)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.comment
    
    def get_absolute_url(self):
        return reverse('article_list')