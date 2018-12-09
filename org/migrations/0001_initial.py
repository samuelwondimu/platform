# Generated by Django 2.1.2 on 2018-12-09 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField()),
                ('location', models.CharField(max_length=255)),
                ('url', models.SlugField(unique=True)),
                ('photo', models.URLField()),
                ('linkedin', models.URLField(blank=True, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('github', models.URLField(blank=True, null=True)),
                ('year_joined', models.DateField()),
                ('alumnus', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['user__user__username'],
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('tagline', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('url', models.URLField()),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='member',
            name='roles',
            field=models.ManyToManyField(to='org.Role'),
        ),
        migrations.AddField(
            model_name='member',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='members', to='org.Team'),
        ),
        migrations.AddField(
            model_name='member',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.User'),
        ),
    ]
