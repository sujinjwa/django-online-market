# Generated by Django 4.1.5 on 2023-01-17 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_member_age'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='member',
            options={'verbose_name': '회원', 'verbose_name_plural': '회원'},
        ),
    ]
