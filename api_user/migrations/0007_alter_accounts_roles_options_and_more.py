# Generated by Django 4.1.1 on 2022-10-06 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_user', '0006_accounts_roles_remove_accounts_role_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='accounts_roles',
            options={},
        ),
        migrations.AlterModelTable(
            name='accounts_roles',
            table='accounts_roles',
        ),
    ]
