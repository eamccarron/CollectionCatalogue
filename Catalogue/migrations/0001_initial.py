# Generated by Django 3.1.7 on 2021-02-27 21:10

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
            name='BaseModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catalogue_num', models.IntegerField(default=5)),
                ('name', models.CharField(default='na', max_length=100)),
                ('date', models.CharField(default='na', max_length=100)),
                ('condition', models.TextField(default='na')),
                ('provenance', models.CharField(default='na', max_length=100)),
                ('description', models.TextField(default='na')),
                ('item_type', models.CharField(default='na', max_length=100)),
                ('staff_creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Fossil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.IntegerField(blank=True, null=True)),
                ('scientific_name', models.CharField(default='na', max_length=100)),
                ('base', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Catalogue.basemodel')),
            ],
        ),
    ]