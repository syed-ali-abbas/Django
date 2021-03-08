from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
            'auth.User',
            on_delete=models.CASCADE,
            )
    body = models.TextField()
    Image = models.ImageField(upload_to='products/', blank=True)

    def __str__(self):
        return self.title

        




