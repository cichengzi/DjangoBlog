# Generated by Django 4.0.1 on 2022-10-14 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_id', models.IntegerField(unique=True)),
                ('doc_class_id', models.IntegerField()),
                ('doc_title', models.CharField(max_length=50)),
                ('doc_content', models.TextField()),
                ('doc_pub_date', models.DateTimeField()),
                ('doc_publisher_id', models.IntegerField(default=1)),
                ('doc_type', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_class_id', models.IntegerField(unique=True)),
                ('doc_class_title', models.CharField(max_length=50)),
            ],
        ),
    ]
