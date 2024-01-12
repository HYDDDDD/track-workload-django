# Generated by Django 5.0.1 on 2024-01-12 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='status',
            field=models.CharField(blank=True, choices=[('P', 'pass'), ('N', 'no pass'), ('D', 'doing')], max_length=1),
        ),
    ]
