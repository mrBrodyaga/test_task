from rest_framework import serializers
from .models import Material, Сategory
from django.db import models

 
class MaterialSerializer(serializers.ModelSerializer):
    """Сериализуем Материалы"""

    class Meta:
        model = Material
        fields = "__all__"


class СategorySerializer(serializers.ModelSerializer):
    """Сериализуем Категории"""

    class Meta:
        model = Сategory
        fields = "__all__"


class CategoryTreeSerializer(serializers.ModelSerializer):
    subcategories = serializers.SerializerMethodField()
    materials = MaterialSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Сategory
        fields = ['id', 'name', 'code_category', 'subcategories', 'materials', 'total_price']

    def get_subcategories(self, obj):
        return CategoryTreeSerializer(obj.subcategories.all(), many=True).data

    def get_total_price(self, obj):
        total = obj.materials.aggregate(total=models.Sum('price'))['total'] or 0
        for sub in obj.subcategories.all():
            sub_total = self.get_total_price(sub)
            total += sub_total
        return total
