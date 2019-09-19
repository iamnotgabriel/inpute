# Generated by Django 2.2.5 on 2019-09-19 00:10

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
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_ra', models.CharField(max_length=30)),
                ('user_course', models.PositiveSmallIntegerField(choices=[(1, 'student'), (2, 'teacher'), (3, 'secretary'), (4, 'supervisor'), (5, 'admin')])),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]