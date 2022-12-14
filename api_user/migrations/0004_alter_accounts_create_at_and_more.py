# Generated by Django 4.1.1 on 2022-09-20 16:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_user', '0003_alter_accounts_create_at_alter_accounts_profile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 20, 16, 10, 44, 488559, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='accounts_infor',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 20, 16, 10, 44, 488559, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='payment_type',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 20, 16, 10, 44, 488559, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='profiles',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 20, 16, 10, 44, 488559, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='profiles_payment_type',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 20, 16, 10, 44, 488559, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='roles',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 20, 16, 10, 44, 488559, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='scopes',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 20, 16, 10, 44, 488559, tzinfo=datetime.timezone.utc)),
        ),
    ]
