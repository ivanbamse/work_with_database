from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/')
    release_date = models.DateField()
    lte_exists = models.BooleanField(default=True)
    slug = models.SlugField(unique=True)
    def __str__(self):
        return self.name

