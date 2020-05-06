# Generated by Django 2.2.3 on 2019-07-26 10:48

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_articlepost_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='avatar',
            field=imagekit.models.fields.ProcessedImageField(upload_to='article/%Y%m%d'),
        ),
    ]
