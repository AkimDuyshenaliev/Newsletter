# Generated by Django 2.2.5 on 2019-09-14 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mailing', '0002_auto_20190914_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savetextfilemodel',
            name='fileTXT',
            field=models.FileField(upload_to='', verbose_name='Upload .txt with emails'),
        ),
    ]
