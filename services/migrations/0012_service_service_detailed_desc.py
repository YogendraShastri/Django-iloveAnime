# Generated by Django 4.2.7 on 2023-12-01 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0011_remove_notification_notice_link_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='service_detailed_desc',
            field=models.TextField(blank=True, null=True),
        ),
    ]
