# Generated by Django 2.2.5 on 2019-09-14 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SaveTextFileModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fileTXT', models.FileField(upload_to='documents/')),
            ],
        ),
    ]
