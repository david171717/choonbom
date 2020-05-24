# Generated by Django 2.2.5 on 2020-05-21 18:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Wedding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_name', models.TextField(default='')),
                ('your_name', models.TextField(default='')),
                ('my_gender', models.BooleanField(default=0)),
                ('your_gender', models.BooleanField(default=0)),
                ('myfather_name', models.TextField(default='', null=True)),
                ('mymother_name', models.TextField(default='', null=True)),
                ('yourfather_name', models.TextField(default='', null=True)),
                ('yourmother_name', models.TextField(default='', null=True)),
                ('wedding_location', models.TextField(default='')),
                ('wedding_date', models.TextField(default='')),
                ('wedding_photo', models.TextField(default='', null=True)),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
