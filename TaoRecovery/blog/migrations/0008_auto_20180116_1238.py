# Generated by Django 2.0 on 2018-01-16 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_post_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, default='static/img/default.png', null=True, upload_to='img'),
        ),
    ]
