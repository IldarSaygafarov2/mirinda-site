# Generated by Django 5.1.1 on 2024-10-01 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_userrequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='userrequest',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата отправки заявки'),
        ),
    ]