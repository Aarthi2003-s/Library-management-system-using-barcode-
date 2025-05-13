# books/models.py
from django.db import models
import barcode
from barcode.writer import ImageWriter
from io import BytesIO
from django.core.files.base import ContentFile
from django.utils import timezone

class Book(models.Model):
    access_no = models.CharField(max_length=20, unique=True, primary_key=True)
    title = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    publication_date = models.IntegerField()
    edition_no=models.CharField(max_length=20,null=True)
    barcode = models.ImageField(upload_to='barcodes/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.barcode:
            code = barcode.get('code128', self.access_no, writer=ImageWriter())
            buffer = BytesIO()
            code.write(buffer)
            self.barcode.save(f'barcode_{self.access_no}.png',
                              ContentFile(buffer.getvalue()),
                              save=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.access_no})"


