# Generated by Django 5.0.6 on 2024-10-06 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cf_app', '0002_user_no_telp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
