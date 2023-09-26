# Generated by Django 4.2.5 on 2023-09-25 16:21

from django.db import migrations, models
import job.models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0016_alter_job_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='images',
            field=models.ImageField(height_field='500', upload_to=job.models.image_upload, width_field='100'),
        ),
    ]
