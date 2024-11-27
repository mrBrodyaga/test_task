from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Сategory(models.Model):
    name = models.CharField(max_length=255, verbose_name="Наименование категории")
    code_category = models.CharField(max_length=50, unique=True, verbose_name="Код категории")
    parent_category = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='subcategories')

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Material(models.Model):
    name = models.CharField(max_length=255, verbose_name="Наименование материала")
    code_material = models.CharField(max_length=50, unique=True, verbose_name="Код материала")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Стоимость материала")
    category = models.ForeignKey(Сategory, on_delete=models.DO_NOTHING, related_name='materials', default=None)

    class Meta:
        verbose_name = "Материал"
        verbose_name_plural = "Материалы"

    def __str__(self):
        return self.name
