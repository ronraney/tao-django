# Generated by Django 2.0 on 2017-12-15 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20171215_0848'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='translator_note',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='translators',
            field=models.ManyToManyField(to='blog.Translator'),
        ),
    ]
