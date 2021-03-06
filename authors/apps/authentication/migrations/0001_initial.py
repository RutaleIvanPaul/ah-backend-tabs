# Generated by Django 2.0.7 on 2018-08-15 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(db_index=True, max_length=255, unique=True)),
                ('email', models.EmailField(db_index=True, max_length=254, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('fb_social_id', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('google_social_id', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('bio', models.CharField(blank=True, max_length=255)),
                ('image', models.ImageField(blank=True, max_length=800, upload_to='profile_image')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
