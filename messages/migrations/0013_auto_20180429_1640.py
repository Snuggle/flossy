# Generated by Django 2.0.4 on 2018-04-29 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messagesapp', '0012_auto_20180429_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='datetime',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
