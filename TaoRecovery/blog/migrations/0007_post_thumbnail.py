# Generated by Django 2.0 on 2018-01-16 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20171215_0910'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, default='/img/default.png', null=True, upload_to='img'),
        ),
    ]
