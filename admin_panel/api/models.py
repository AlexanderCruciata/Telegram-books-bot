from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
import os

from rest_framework.fields import uuid


class BookCategory(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.category_name


class Book(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="books_images/")
    category = models.ForeignKey(BookCategory, models.CASCADE)

    def save(self, *args, **kwargs):
        if self.image:
            unique_code = uuid.uuid4().hex[:8]
            file_extension = os.path.splitext(self.image.name)
            new_filename = f"book_{self.name}_{unique_code}{file_extension[-1]}"
            self.image.name = new_filename
        super(Book, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name


@receiver(pre_save, sender=BookCategory)
def category_save(sender, instance, **kwargs):
    pass