# Generated by Django 5.0.2 on 2024-03-29 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_user_bio_user_name_alter_user_email'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Workers',
        ),
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=200),
        ),
    ]
