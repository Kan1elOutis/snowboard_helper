from django.db import models

from users.models import User


class RidingStyle(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'riding_style'
        verbose_name_plural = 'riding_stylies'

    def __str__(self):
        return self.name


class Resume(models.Model):
    first_name = models.CharField(max_length=256, default='Иван')
    last_name = models.CharField(max_length=256, default='Иванов')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='resumes_images')
    riding_style = models.ForeignKey(to=RidingStyle, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'resume'
        verbose_name_plural = 'resumes'

    def __str__(self):
        return f'{self.first_name} {self.last_name} | {self.riding_style.name}'


class Record(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, default=1)
    fio = models.CharField(max_length=256, default='Иванов Иван Иванович')
    phone = models.IntegerField(null=False, unique=True)
    date = models.DateTimeField()
    instructor = models.ForeignKey(to=Resume, on_delete=models.CASCADE)

    def __str__(self):
        return f'Заказ у {self.instructor.first_name} {self.instructor.last_name} дата: {self.date}'
