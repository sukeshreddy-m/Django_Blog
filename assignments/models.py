from django.db import models

class about(models.Model):
    about_head = models.CharField(max_length=25)
    about_description = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.about_head
    
class social(models.Model):
    platform = models.CharField(max_length=50)
    link = models.URLField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.platform