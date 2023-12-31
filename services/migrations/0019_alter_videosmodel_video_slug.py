# Generated by Django 4.2.7 on 2023-12-02 17:27

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0018_rename_title_videosmodel_video_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videosmodel',
            name='video_slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='video_title', unique=True),
        ),
    ]
