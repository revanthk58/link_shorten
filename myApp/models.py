from django.db import models
import random
import string

class URL(models.Model):
    original_url = models.URLField()
    short_url = models.CharField(max_length=10, unique=True)

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = self.generate_short_url()
        super().save(*args, **kwargs)

    def generate_short_url(self):
        length = 4
        characters = string.ascii_letters + string.digits
        short_url = ''.join(random.choice(characters) for _ in range(length))
        return "revanth"+short_url

    def __str__(self):
        return f"{self.original_url} -> {self.short_url}"
