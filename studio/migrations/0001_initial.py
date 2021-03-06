# Generated by Django 2.0 on 2017-12-13 12:34

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Studio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('location', models.CharField(max_length=60)),
                ('studio_image', models.ImageField(null=True, upload_to='posts/')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, default=True, max_length=30)),
                ('description', models.CharField(max_length=120)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('pic', models.ImageField(upload_to='posts/')),
            ],
        ),
        migrations.CreateModel(
            name='things',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('pic', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='studio',
            name='tags',
            field=models.ManyToManyField(to='studio.tags'),
        ),
        migrations.AddField(
            model_name='studio',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studio.User'),
        ),
    ]
