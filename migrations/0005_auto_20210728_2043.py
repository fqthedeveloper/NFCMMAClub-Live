# Generated by Django 3.2.4 on 2021-07-28 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NFCapp', '0004_page'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quest', models.TextField()),
                ('ans', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('detail', models.TextField()),
                ('img', models.ImageField(null=True, upload_to='services/')),
            ],
        ),
        migrations.DeleteModel(
            name='Service',
        ),
    ]
