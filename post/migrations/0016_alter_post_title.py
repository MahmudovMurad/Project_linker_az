# Generated by Django 4.0.1 on 2022-05-17 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0015_remove_post_post_views_post_view_count_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Qrupun adı'),
        ),
    ]
