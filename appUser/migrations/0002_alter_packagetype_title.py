# Generated by Django 4.1.5 on 2023-06-04 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appUser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packagetype',
            name='title',
            field=models.CharField(max_length=50, null=True, verbose_name='Paket Adı'),
        ),
    ]