# Generated by Django 2.2.12 on 2022-03-24 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='test_Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'test_Publication',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='test_Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=100)),
                ('publications', models.ManyToManyField(to='comment.test_Publication')),
            ],
            options={
                'db_table': 'test_Article',
                'ordering': ['headline'],
            },
        ),
    ]