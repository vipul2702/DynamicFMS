# Generated by Django 4.1.9 on 2023-06-17 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_studentadmission_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentadmission',
            name='graduationmarks',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='studentadmission',
            name='highmarks',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='studentadmission',
            name='intermarks',
            field=models.FloatField(),
        ),
    ]
