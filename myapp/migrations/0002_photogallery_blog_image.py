# Generated by Django 5.0.6 on 2024-05-18 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='default_image.jpg', upload_to='images/'),
        ),
    ]
