# Generated by Django 3.2.9 on 2021-11-15 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='addProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('P_name', models.CharField(max_length=25)),
                ('P_code', models.CharField(max_length=25)),
                ('P_category', models.CharField(max_length=25)),
                ('P_price', models.IntegerField()),
                ('P_quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='addReturn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('P_name', models.CharField(max_length=25)),
                ('P_code', models.CharField(max_length=25)),
                ('P_category', models.CharField(max_length=25)),
                ('P_quantity', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='registerd_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=25)),
                ('mobile', models.CharField(max_length=13)),
                ('user_type', models.CharField(max_length=13)),
                ('username', models.CharField(max_length=25)),
                ('password1', models.CharField(max_length=25)),
                ('password2', models.CharField(max_length=25)),
            ],
        ),
    ]
