# Generated by Django 3.1.4 on 2021-01-23 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0004_auto_20210109_2208'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='parents',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tweets.tweet'),
        ),
    ]
