# Generated by Django 3.1.1 on 2021-03-02 09:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='კომენტარი')),
            ],
            options={
                'verbose_name_plural': 'პოსტის კომენტარები',
            },
        ),
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leagues', models.CharField(max_length=100, unique=True, verbose_name='ჩემპიონატის სახელი')),
                ('image', models.ImageField(upload_to='images', verbose_name='ჩემპიონატის ლოგო')),
            ],
            options={
                'verbose_name_plural': 'ჩემპიონატები და გუნდები',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='სათაური')),
                ('short_desc', models.TextField(verbose_name='მოკლე აღწერა')),
                ('desc', models.TextField(verbose_name='აღწერა')),
                ('see_home_page', models.BooleanField(default=False, verbose_name='დადასტურება')),
                ('image', models.ImageField(upload_to='images', verbose_name='სურათი')),
                ('league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.league', verbose_name='ჩემპიონატი')),
            ],
            options={
                'verbose_name_plural': 'სიახლეები',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teams', models.CharField(max_length=70, unique=True, verbose_name='გუნდის სახელი')),
                ('image', models.ImageField(upload_to='images', verbose_name='გუნდის ლოგო')),
                ('league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.league', verbose_name='ჩემპიონატი, რომელშიც გუნდი თამაშობს')),
            ],
        ),
        migrations.CreateModel(
            name='ReplyComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='კომენტარი')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.post', verbose_name='პოსტი')),
                ('reply_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='კომენტრის ავტორი')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='post',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.team', verbose_name='გუნდი'),
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='სიახლის ავტორი'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.post', verbose_name='პოსტი'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='კომენტრის ავტორი'),
        ),
    ]