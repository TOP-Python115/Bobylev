# Generated by Django 4.1.3 on 2022-11-12 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_alter_card_picture_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='counter',
            field=models.SmallIntegerField(default=0),
        ),
    ]