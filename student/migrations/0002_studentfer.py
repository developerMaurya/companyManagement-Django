# Generated by Django 3.0.2 on 2020-12-22 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='studentfer',
            fields=[
                ('stdudeid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('father_name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=20)),
                ('qualification', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('mobile', models.IntegerField()),
                ('email', models.CharField(max_length=20)),
                ('fullmarks', models.IntegerField()),
                ('obtaindmarks', models.IntegerField()),
                ('grad', models.CharField(max_length=20)),
                ('percentage', models.CharField(max_length=20)),
                ('attendance', models.CharField(max_length=20)),
                ('studenttype', models.CharField(max_length=20)),
                ('performance', models.CharField(max_length=20)),
                ('studeimage', models.ImageField(upload_to='')),
            ],
        ),
    ]
