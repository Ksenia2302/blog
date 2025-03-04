# Generated by Django 5.1.1 on 2024-09-25 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='image_new')),
                ('description', models.TextField()),
                ('full_text', models.TextField()),
                ('date_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
