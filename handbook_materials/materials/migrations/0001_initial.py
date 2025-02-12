# Generated by Django 5.1.3 on 2024-11-18 11:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Сategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование категории')),
                ('code_category', models.CharField(max_length=50, unique=True, verbose_name='Код категории')),
                ('subcategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_category', to='materials.сategory')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование материала')),
                ('code_material', models.CharField(max_length=50, unique=True, verbose_name='Код материала')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Стоимость материала')),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, related_name='materials', to='materials.сategory')),
            ],
            options={
                'verbose_name': 'Материал',
                'verbose_name_plural': 'Материалы',
                'ordering': ('name',),
            },
        ),
    ]
