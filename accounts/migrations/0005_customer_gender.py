# Generated by Django 3.0.8 on 2020-07-27 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200726_1852'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'آقا'), ('Female', 'خانم')], max_length=6, null=True),
        ),
    ]