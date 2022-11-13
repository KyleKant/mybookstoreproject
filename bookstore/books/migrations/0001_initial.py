# Generated by Django 3.2 on 2021-05-07 13:31

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
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_book', models.CharField(max_length=30)),
                ('author', models.CharField(max_length=30)),
                ('illumination', models.ImageField(height_field='img_height', upload_to='', width_field='img_width')),
                ('img_height', models.IntegerField(default=1)),
                ('img_width', models.IntegerField(default=1)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(default=True, null=True)),
                ('category', models.CharField(default='Fairy Tale', max_length=100)),
                ('content_summary', models.TextField(default='Type book summary')),
                ('status', models.CharField(default='in progress', max_length=30)),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('upload_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_chapter', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('content_chapter', models.TextField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chapters', to='books.book')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chapters', to=settings.AUTH_USER_MODEL)),
                ('update_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Content_Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_updated', models.DateTimeField(auto_now_add=True)),
                ('content_chapter', models.TextField()),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='content_chapters', to='books.chapter')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_category', models.CharField(max_length=30)),
                ('book', models.ManyToManyField(related_name='categories', to='books.Book')),
            ],
        ),
    ]
