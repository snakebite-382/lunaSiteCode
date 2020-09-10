# Generated by Django 3.1 on 2020-09-10 22:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=120)),
                ('author', models.CharField(default='Anonymous', max_length=120)),
                ('rating', models.CharField(choices=[('1S', '1 star'), ('2S', '2 star'), ('3S', '3 star'), ('4S', '4 star'), ('5S', '5 star')], default='1 star', max_length=120)),
                ('body', models.TextField()),
                ('featured', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('createdOn', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
