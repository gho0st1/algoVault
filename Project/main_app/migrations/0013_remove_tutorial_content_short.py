# Generated by Django 3.2.8 on 2022-01-01 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_alter_tutorial_content_short'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutorial',
            name='content_short',
        ),
    ]