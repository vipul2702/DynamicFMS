# Generated by Django 4.1.9 on 2023-12-02 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_alter_fee_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrolledstudent',
            name='fname',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='enrolledstudent',
            name='mname',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
