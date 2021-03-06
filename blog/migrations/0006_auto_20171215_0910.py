# Generated by Django 2.0 on 2017-12-15 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_book_first_edition'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='source_author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='source_translator',
        ),
        migrations.AddField(
            model_name='post',
            name='source_authors',
            field=models.ManyToManyField(null=True, to='blog.Writer'),
        ),
        migrations.AddField(
            model_name='post',
            name='source_translators',
            field=models.ManyToManyField(null=True, to='blog.Translator'),
        ),
    ]
