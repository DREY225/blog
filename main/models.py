from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='article/image')
    created_at = models.DateTimeField(auto_now_add=True)
    uploaded_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'article'
        verbose_name = 'Article' 
        verbose_name_plural = 'Articles'
    
    
