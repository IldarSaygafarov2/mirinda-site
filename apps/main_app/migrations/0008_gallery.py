# Generated by Django 5.1.1 on 2024-09-30 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_companyvalue'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='gallery/', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Галлерея',
                'verbose_name_plural': 'Галлерея',
            },
        ),
    ]
