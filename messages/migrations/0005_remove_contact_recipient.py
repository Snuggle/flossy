# Generated by Django 2.0.4 on 2018-04-29 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messagesapp', '0004_remove_contact_sender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='recipient',
        ),
    ]
