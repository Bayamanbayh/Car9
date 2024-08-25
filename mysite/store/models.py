from django.db import models

class Marka(models.Model):
    marka_name = models.CharField(max_length=16)

    def __str__(self):
        return self.marka_name

class Car(models.Model):
    product_name = models.CharField(max_length=32)
    description = models.TextField()
    year = models.DecimalField(max_digits=5, decimal_places=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=16)
    volume = models.DecimalField(max_digits=2, decimal_places=1)
    category = models.ForeignKey(Marka, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)
    have = models.BooleanField(default=True)
    video = models.FileField(upload_to='videos/', null=True, blank=True)


class CarModel(models.Model):
    car_model = models.CharField(max_length=16),
    text = models.TextField
    car_marka = models.ForeignKey(Marka, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return f'{self.car_model} - {self.car_marka}'

class CarPhotos(models.Model):
    product = models.ForeignKey(Car, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='img/')
