# Generated by Django 3.2.4 on 2021-08-02 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NFCapp', '0013_rename_gallery_galleryimage_gallery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleryimage',
            name='img',
            field=models.ImageField(null=True, upload_to='gallery_imgs/'),
        ),
    ]
