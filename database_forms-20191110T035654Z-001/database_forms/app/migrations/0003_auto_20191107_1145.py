# Generated by Django 2.2.7 on 2019-11-07 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20191107_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='mahadiscom',
            name='content',
            field=models.TextField(default='none'),
        ),
        migrations.AddField(
            model_name='mahadiscom',
            name='title',
            field=models.CharField(default=0, max_length=300),
            preserve_default=False,
        ),
    ]
