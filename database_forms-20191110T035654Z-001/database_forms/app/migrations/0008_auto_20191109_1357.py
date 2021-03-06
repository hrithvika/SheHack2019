# Generated by Django 2.2.7 on 2019-11-09 13:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0007_auto_20191108_0654'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField(default=0)),
                ('country', models.CharField(default='India', max_length=30)),
                ('diet', models.IntegerField(default=0)),
                ('car_fuel', models.IntegerField(default=0)),
                ('scooter', models.IntegerField(default=0)),
                ('family', models.IntegerField(default=0)),
                ('electricity', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='MahaDiscom',
        ),
    ]
