# Generated by Django 5.1.3 on 2024-12-07 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_donation_status_alter_volunteer_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gallery',
            old_name='donationn',
            new_name='donation',
        ),
        migrations.AlterField(
            model_name='donation',
            name='updationdate',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
