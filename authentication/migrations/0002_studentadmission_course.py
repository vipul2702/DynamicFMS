# Generated by Django 4.1.9 on 2023-06-17 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentadmission',
            name='course',
            field=models.CharField(max_length=20, null=True),
        ),
    ]