# Generated by Django 5.2.4 on 2025-07-23 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_enforce_default_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True, unique=True),
        ),
    ]
