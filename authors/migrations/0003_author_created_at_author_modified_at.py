# Generated by Django 5.1.2 on 2024-11-23 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0002_alter_author_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='modified_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
