from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    Image = models.ImageField(upload_to='projects/')
    link = models.URLField(blank=True)

    def _str_ (self):
        return self.title