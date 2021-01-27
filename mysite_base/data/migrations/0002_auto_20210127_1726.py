# Generated by Django 3.1.5 on 2021-01-27 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eco',
            name='link',
        ),
        migrations.RemoveField(
            model_name='it',
            name='link',
        ),
        migrations.RemoveField(
            model_name='sports',
            name='link',
        ),
        migrations.AddField(
            model_name='eco',
            name='crawled_time',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='eco',
            name='preview',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='eco',
            name='writer',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='it',
            name='crawled_time',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='it',
            name='preview',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='it',
            name='writer',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sports',
            name='crawled_time',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sports',
            name='preview',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='eco',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='it',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='sports',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]