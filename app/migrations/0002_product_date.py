# Generated by Django 4.2.7 on 2024-02-04 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]