# Generated by Django 4.1.9 on 2023-10-22 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_remove_course_id_remove_fee_totalfee_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_code',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]