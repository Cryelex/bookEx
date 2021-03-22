# Generated by Django 3.1 on 2020-11-29 22:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookMng', '0003_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='purchased',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='book',
            name='shopping_cart_user',
            field=models.ManyToManyField(blank=True, related_name='assignee', to=settings.AUTH_USER_MODEL),
        ),
    ]