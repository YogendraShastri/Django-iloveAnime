# Generated by Django 4.2.7 on 2023-12-02 03:58

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0014_notification_notice_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='service_slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='service_title', unique=True),
        ),
    ]