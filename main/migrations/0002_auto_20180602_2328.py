# Generated by Django 2.0.6 on 2018-06-02 22:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, max_length=200, null=True)),
                ('thumbnail', models.ImageField(upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='sport',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Sport'),
        ),
    ]
