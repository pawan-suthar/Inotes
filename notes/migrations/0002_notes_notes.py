# Generated by Django 4.1.7 on 2023-05-14 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='notes',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
