# Generated by Django 2.0.5 on 2018-05-14 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='icon',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
    ]
