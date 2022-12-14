# Generated by Django 3.2 on 2021-05-07 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='content_summary',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='book',
            name='img_height',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='book',
            name='img_width',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='book',
            name='updated_at',
            field=models.DateTimeField(null=True),
        ),
    ]
