from django.db import models

# Create your models here.

class Movie(models.Model):
    isim = models.CharField(max_length = 50)
    aciklama = models.TextField()
    yuklenme_tarih = models.DateTimeField(auto_now_add = True)
    resim = models.FileField(upload_to='resimler/', verbose_name="Film Resmi", null=True, blank=True)

    def __str__(self):
        return self.isim