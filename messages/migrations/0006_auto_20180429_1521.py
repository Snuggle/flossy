# Generated by Django 2.0.4 on 2018-04-29 15:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('messagesapp', '0005_remove_contact_recipient'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='contact',
            field=models.CharField(default='0000000', max_length=100),
        ),
        migrations.AddField(
            model_name='contact',
            name='owner',
            field=models.ForeignKey(default='0000000', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]