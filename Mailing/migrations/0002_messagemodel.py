# Generated by Django 2.2.5 on 2019-12-21 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Mailing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sendDate', models.DateField()),
                ('subject', models.CharField(default='', max_length=80)),
                ('message', models.TextField(default='')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Mailing.DepartmentModel')),
            ],
        ),
    ]
