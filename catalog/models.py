from django.db import models


class Category(models.Model):
    name = models.CharField('Название категории', max_length=100, )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('name',)


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField('Название продукта', max_length=100)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()
    productivity = models.DecimalField(default=True, max_digits=10, decimal_places=2)
    price = models.DecimalField(default=True ,max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('name',)
        index_together = (('id',),)


