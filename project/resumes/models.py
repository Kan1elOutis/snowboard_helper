from django.db import models


class RidingStyle(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'riding_style'
        verbose_name_plural = 'riding_stylies'

    def __str__(self):
        return self.name


class Resume(models.Model):
    first_name = models.CharField(max_length=256, unique=True)
    last_name = models.CharField(max_length=256, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='products_images')
    riding_style = models.ForeignKey(to=RidingStyle, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'resume'
        verbose_name_plural = 'resumes'

    def __str__(self):
        return f'Резюме: {self.name} | Стиль катания: {self.riding_style.name}'
