# Generated by Django 2.1 on 2018-09-04 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vfb_server', '0008_auto_20180904_1008'),
    ]

    operations = [
        migrations.RenameField(
            model_name='neuron',
            old_name='external_identifiers',
            new_name='external_identifier',
        ),
        migrations.RenameField(
            model_name='neuronsimple',
            old_name='external_identifiers',
            new_name='external_identifier',
        ),
    ]