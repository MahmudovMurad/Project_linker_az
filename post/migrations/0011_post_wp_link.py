# Generated by Django 3.2.9 on 2022-02-10 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0010_auto_20220208_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='wp_link',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='linker wp number'),
        ),
    ]
