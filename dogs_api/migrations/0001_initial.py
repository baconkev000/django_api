# Generated by Django 3.2.13 on 2022-06-24 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DogInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breed', models.CharField(max_length=500)),
                ('org_img', models.CharField(max_length=500)),
                ('mod_img', models.CharField(max_length=500)),
            ],
        ),
    ]
