# Generated by Django 4.1.7 on 2023-05-17 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appCategory', '0003_alter_subcategory_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, null=True, verbose_name='Category Slug'),
        ),
    ]