from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва категорії")

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=200, verbose_name="Назва страви")
    description = models.TextField(verbose_name="Опис")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Ціна")
    available = models.BooleanField(default=True, verbose_name="Доступна")

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="dishes",
        verbose_name="Категорія"
    )

    class Meta:
        verbose_name = "Страва"
        verbose_name_plural = "Страви"

    def __str__(self):
        return self.name