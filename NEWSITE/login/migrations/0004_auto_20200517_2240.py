# Generated by Django 3.0.5 on 2020-05-17 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20200517_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='time',
            field=models.CharField(choices=[('8.30-10.00', '8.30-10.00'), ('10.10-11.40', '10.10-11.40'), ('11.50-13.20', '11.50-13.20')], max_length=30, null=True),
        ),
    ]
