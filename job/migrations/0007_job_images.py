# Generated by Django 4.2.5 on 2023-09-23 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_job_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='images',
            field=models.ImageField(default=1, upload_to='jobs/'),
            preserve_default=False,
        ),
    ]
