# Generated by Django 2.2.3 on 2019-07-16 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogindex', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='feature_image',
            field=models.ImageField(default='', upload_to='images/'),
        ),
    ]
