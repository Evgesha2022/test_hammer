# Generated by Django 4.2.3 on 2023-08-18 15:53

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('auth_user', '0002_alter_profile_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default=None, max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Enter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inv_code', models.CharField(default=None, max_length=6)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None, unique=True)),
            ],
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='inv_code',
            new_name='inv_code_fr',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='phone_number',
        ),
    ]
