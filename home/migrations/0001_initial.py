# Generated by Django 5.1.1 on 2024-09-30 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
                ('student_email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
