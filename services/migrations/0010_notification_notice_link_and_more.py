# Generated by Django 4.2.7 on 2023-12-01 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0009_remove_service_service_detailed_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='Notice_link',
            field=models.URLField(default=None,null=True),
        ),
        migrations.AlterField(
            model_name='notification',
            name='Notification_desc',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='notification',
            name='Notification_icon',
            field=models.FileField(default=None, max_length=300, upload_to='images/'),
        ),
    ]