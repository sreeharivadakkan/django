# Generated by Django 2.2.7 on 2019-12-02 09:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20191202_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 2, 15, 17, 51, 35178), verbose_name='date published'),
        ),
    ]
