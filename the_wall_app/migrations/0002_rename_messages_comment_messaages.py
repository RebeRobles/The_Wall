# Generated by Django 3.2.6 on 2021-09-21 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('the_wall_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='messages',
            new_name='messaages',
        ),
    ]