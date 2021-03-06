# Generated by Django 2.1 on 2018-11-27 15:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('log_sign_app', '0003_auto_20181124_1443'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserModelProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portfolio_site', models.URLField(blank=True)),
                ('portfile_pic', models.ImageField(blank=True, upload_to='pics')),
                ('user', models.OneToOneField(on_delete='models.CASCADE', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='LogIn',
        ),
        migrations.DeleteModel(
            name='SignUp',
        ),
    ]
