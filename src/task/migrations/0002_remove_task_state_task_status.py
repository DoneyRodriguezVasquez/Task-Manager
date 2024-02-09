# Generated by Django 4.2.8 on 2024-02-04 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='state',
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('TO_DO', 'TO DO'), ('IN_PROGRESS', 'IN PROGRESS'), ('DONE', 'DONE')], default='TO_DO', max_length=20),
        ),
    ]
