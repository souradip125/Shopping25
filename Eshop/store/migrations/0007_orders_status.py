# Generated by Django 3.2.8 on 2021-10-20 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20211020_2051'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]