# Generated by Django 2.1.7 on 2019-04-16 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20190308_1842'),
    ]

    operations = [
        migrations.CreateModel(
            name='nustartup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(default='insert')),
                ('team', models.TextField(default='insert')),
                ('logo', models.ImageField(blank=True, default='default.jpg', upload_to='events')),
                ('url', models.CharField(max_length=255)),
            ],
        ),
    ]