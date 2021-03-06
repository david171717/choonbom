# Generated by Django 2.2.5 on 2020-05-31 08:51

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
                ('my_name', models.TextField(null=True)),
                ('your_name', models.TextField(null=True)),
                ('my_gender', models.IntegerField(null=True)),
                ('your_gender', models.IntegerField(null=True)),
                ('myfather_name', models.TextField(null=True)),
                ('mymother_name', models.TextField(null=True)),
                ('yourfather_name', models.TextField(null=True)),
                ('yourmother_name', models.TextField(null=True)),
                ('wedding_location', models.TextField(null=True)),
                ('wedding_date', models.TextField(null=True)),
                ('wedding_photo', models.TextField(null=True)),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
