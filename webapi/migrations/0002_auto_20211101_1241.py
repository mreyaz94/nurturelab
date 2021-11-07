# Generated by Django 3.1.4 on 2021-11-01 12:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking_db',
            name='schedule_time',
        ),
        migrations.AlterField(
            model_name='booking_db',
            name='booked_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='booking_db',
            name='booking_time',
            field=models.DateTimeField(),
        ),
    ]