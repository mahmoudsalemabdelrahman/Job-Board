# Generated by Django 4.2.5 on 2023-09-25 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0012_apply_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='published_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]