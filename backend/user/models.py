from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    # Authentication fields might be added later, for now only username is defined for filtering purposes.
    
    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = "Users"
        ordering = ['username']
        unique_together = ('username',)