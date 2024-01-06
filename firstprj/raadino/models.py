from django.db import models

class model_blog(models.Model):
    title =models.CharField(max_length=100)
    slug = models.SlugField()
    author=models.CharField(max_length=100)
    body=models.TextField()
    img=models.ImageField(default='default.jpg',blank=True)
    created_at=models.CharField(max_length=100)
    updated_at=models.DateTimeField(auto_now_add=True)
    date=models.DateTimeField(auto_now_add=True)
   
   
    def __str__(self):
        return self.title
    
    def snippet(self):
        return self.body[:50] + '...'
    