from django.db import models

class Category(models.Model):
    TYPE_CHOICES = [
        ('income', 'income'),
        ('expense', 'expense'),
        ('transfer', 'transfer'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']
        unique_together = ('name', 'type')