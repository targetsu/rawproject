# Generated by Django 2.2.5 on 2019-09-20 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField(blank=True, max_length=10, null=True)),
                ('mobile', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
