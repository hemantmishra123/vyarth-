# Generated by Django 3.2.12 on 2022-03-25 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='submitwaste',
            name='number',
            field=models.IntegerField(null=True),
        ),
    ]
