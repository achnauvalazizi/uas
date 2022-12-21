from django.db import models

# Create your models here.

class About(models.Model):
    judul = models.CharField(max_length=50)
    konten = models.TextField()

    def _str_(self):
        return self.judul


class komen(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE)
    konten = models.CharField(max_length=100)

    def _str_(self):
        return self.konten