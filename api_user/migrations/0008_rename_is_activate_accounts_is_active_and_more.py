# Generated by Django 4.1.1 on 2022-10-06 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_user', '0007_alter_accounts_roles_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accounts',
            old_name='is_activate',
            new_name='is_active',
        ),
        migrations.RenameField(
            model_name='accounts_roles',
            old_name='is_activate',
            new_name='is_active',
        ),
        migrations.RenameField(
            model_name='payment_type',
            old_name='is_activate',
            new_name='is_active',
        ),
        migrations.RenameField(
            model_name='profiles',
            old_name='is_activate',
            new_name='is_active',
        ),
        migrations.RenameField(
            model_name='profiles_payment_type',
            old_name='is_activate',
            new_name='is_active',
        ),
        migrations.RenameField(
            model_name='roles',
            old_name='is_activate',
            new_name='is_active',
        ),
    ]
