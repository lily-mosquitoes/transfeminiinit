# Generated by Django 3.2 on 2022-01-16 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20220116_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posttranslation',
            name='description',
            field=models.CharField(blank=True, max_length=170, verbose_name='post_description'),
        ),
        migrations.AlterField(
            model_name='posttranslation',
            name='slug',
            field=models.SlugField(max_length=70, unique_for_date='publish', verbose_name='post_slug'),
        ),
        migrations.AlterField(
            model_name='posttranslation',
            name='title',
            field=models.CharField(max_length=70, verbose_name='post_title'),
        ),
    ]
