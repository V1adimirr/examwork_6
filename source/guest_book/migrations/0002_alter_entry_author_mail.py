# Generated by Django 4.0.5 on 2022-07-02 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guest_book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='author_mail',
            field=models.CharField(max_length=50, verbose_name='Почта'),
        ),
    ]
