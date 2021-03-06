# Generated by Django 2.0.7 on 2018-08-15 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('slug', models.SlugField(blank=True, max_length=255)),
                ('body', models.TextField()),
                ('created_at', models.DateTimeField(editable=False)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('favorited', models.BooleanField(default=False)),
                ('favoritesCount', models.IntegerField(default=0)),
                ('rating', models.PositiveIntegerField(blank=True, editable=False, null=True)),
                ('likesCount', models.IntegerField(default=0)),
                ('dislikesCount', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='ArticleImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('article', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='article_ratings', to='articles.Article')),
            ],
            options={
                'ordering': ('-amount',),
            },
        ),
    ]
