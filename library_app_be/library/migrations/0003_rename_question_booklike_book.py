# Generated by Django 4.1.2 on 2022-10-11 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_booklike'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booklike',
            old_name='question',
            new_name='book',
        ),
    ]