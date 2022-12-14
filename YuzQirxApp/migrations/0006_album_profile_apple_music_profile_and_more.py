# Generated by Django 4.0.6 on 2022-07-29 01:50

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('YuzQirxApp', '0005_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('author', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField()),
                ('executive_producer', models.CharField(blank=True, max_length=255, null=True)),
                ('cover_designer', models.CharField(blank=True, max_length=255, null=True)),
                ('cover', models.ImageField(blank=True, null=True, upload_to='music/covers')),
                ('spotify_link', models.CharField(blank=True, max_length=255, null=True)),
                ('youtube_link', models.CharField(blank=True, max_length=255, null=True)),
                ('soundcloud_link', models.CharField(blank=True, max_length=255, null=True)),
                ('deezer_link', models.CharField(blank=True, max_length=255, null=True)),
                ('apple_music_link', models.CharField(blank=True, max_length=255, null=True)),
                ('yandex_music_link', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='apple_music_profile',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='deezer_profile',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='facebook_profile',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='instagram_profile',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='soundcloud_profile',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='spotify_profile',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='twitter_profile',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='profile',
            name='yandex_music_profile',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='youtube_profile',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='track',
            name='album',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='track',
            name='demo',
            field=models.FileField(default=django.utils.timezone.now, upload_to='demolar/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='track',
            name='created_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='track',
            name='lyrics',
            field=ckeditor.fields.RichTextField(blank=True, max_length=10000, null=True),
        ),
    ]
