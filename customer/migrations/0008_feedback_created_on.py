# Generated by Django 3.2.9 on 2021-12-08 08:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0007_feedback_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
