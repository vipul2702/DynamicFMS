# Generated by Django 4.1.9 on 2023-06-12 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_studentadmission_gender_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coursename', models.CharField(max_length=100)),
                ('courseduration', models.CharField(max_length=100)),
                ('coursedescription', models.TextField()),
            ],
        ),
    ]
