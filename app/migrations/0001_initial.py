# Generated by Django 4.1.2 on 2022-10-18 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QRCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('qr_code', models.ImageField(blank=True, null=True, upload_to='qr_codes/')),
            ],
        ),
    ]
