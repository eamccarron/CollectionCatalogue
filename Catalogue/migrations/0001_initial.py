# Generated by Django 3.1.5 on 2021-04-13 02:21

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
            name='allModels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_type', models.CharField(choices=[('Artwork', 'Artwork'), ('Book', 'Book'), ('Coin', 'Coin'), ('Fossil', 'Fossil'), ('Jewelry', 'Jewelry'), ('Medal', 'Medal'), ('Meteorite', 'Meteorite'), ('Photo', 'Photo'), ('Pottery', 'Pottery'), ('Sculpture', 'Sculpture'), ('Weapon', 'Weapon')], max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_name', models.CharField(max_length=100)),
                ('attribute_content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='OptionalAttributes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_1', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='attr_1', to='Catalogue.attribute')),
                ('attribute_10', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='attr_10', to='Catalogue.attribute')),
                ('attribute_2', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='attr_2', to='Catalogue.attribute')),
                ('attribute_3', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='attr_3', to='Catalogue.attribute')),
                ('attribute_4', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='attr_4', to='Catalogue.attribute')),
                ('attribute_5', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='attr_5', to='Catalogue.attribute')),
                ('attribute_6', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='attr_6', to='Catalogue.attribute')),
                ('attribute_7', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='attr_7', to='Catalogue.attribute')),
                ('attribute_8', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='attr_8', to='Catalogue.attribute')),
                ('attribute_9', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='attr_9', to='Catalogue.attribute')),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('catalogue_num', models.IntegerField(default=1, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('date', models.CharField(blank=True, max_length=100, null=True)),
                ('condition', models.TextField(blank=True, null=True)),
                ('provenance', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('item_type', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(default='catalogue_pics/null.PNG', upload_to='catalogue_pics')),
                ('optional_attribute', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Catalogue.optionalattributes')),
                ('staff_creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(blank=True, max_length=100, null=True)),
                ('weapon_type', models.CharField(blank=True, max_length=100, null=True)),
                ('combat', models.CharField(blank=True, max_length=100, null=True)),
                ('size', models.IntegerField(blank=True, null=True)),
                ('weight', models.IntegerField(blank=True, null=True)),
                ('material', models.CharField(blank=True, max_length=100, null=True)),
                ('record', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Catalogue.record')),
            ],
        ),
        migrations.CreateModel(
            name='Sculpture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.CharField(blank=True, max_length=100, null=True)),
                ('artist', models.CharField(blank=True, max_length=100, null=True)),
                ('colour', models.CharField(blank=True, max_length=100, null=True)),
                ('record', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Catalogue.record')),
            ],
        ),
        migrations.CreateModel(
            name='Pottery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(blank=True, max_length=100, null=True)),
                ('artist_lifespan', models.TextField(blank=True, null=True)),
                ('material', models.CharField(blank=True, max_length=100, null=True)),
                ('technique', models.TextField(blank=True, null=True)),
                ('record', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Catalogue.record')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photographer', models.CharField(blank=True, max_length=100, null=True)),
                ('record', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Catalogue.record')),
            ],
        ),
        migrations.CreateModel(
            name='Meteorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.IntegerField(blank=True, null=True)),
                ('weight', models.IntegerField(blank=True, null=True)),
                ('colour', models.CharField(blank=True, max_length=100, null=True)),
                ('material', models.CharField(blank=True, max_length=100, null=True)),
                ('record', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Catalogue.record')),
            ],
        ),
        migrations.CreateModel(
            name='Medal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medal_type', models.CharField(blank=True, max_length=100, null=True)),
                ('colour', models.CharField(blank=True, max_length=100, null=True)),
                ('material', models.CharField(blank=True, max_length=100, null=True)),
                ('design', models.TextField(blank=True, null=True)),
                ('recipient', models.TextField(blank=True, null=True)),
                ('record', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Catalogue.record')),
            ],
        ),
        migrations.CreateModel(
            name='Jewelry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jewelry_type', models.CharField(choices=[('Pendant', 'Pendant'), ('Bracelet', 'Bracelet'), ('Cufflink', 'Cufflink'), ('Earrings', 'Earrings'), ('Necklace', 'Necklace'), ('Ring', 'Ring'), ('Brooche', 'Brooche'), ('Gem', 'Gem'), ('Other', 'Other')], max_length=10)),
                ('colour', models.CharField(blank=True, max_length=100, null=True)),
                ('material', models.CharField(blank=True, max_length=100, null=True)),
                ('size', models.IntegerField(blank=True, null=True)),
                ('weight', models.IntegerField(blank=True, null=True)),
                ('record', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Catalogue.record')),
            ],
        ),
        migrations.CreateModel(
            name='Fossil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.IntegerField(blank=True, null=True)),
                ('scientific_name', models.CharField(blank=True, max_length=100, null=True)),
                ('record', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Catalogue.record')),
            ],
        ),
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('colour', models.CharField(blank=True, max_length=100, null=True)),
                ('material', models.CharField(blank=True, max_length=100, null=True)),
                ('coin_value', models.CharField(blank=True, max_length=100, null=True)),
                ('design', models.TextField(blank=True, null=True)),
                ('record', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Catalogue.record')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.TextField(blank=True, null=True)),
                ('illustrator', models.TextField(blank=True, null=True)),
                ('language', models.CharField(blank=True, max_length=100, null=True)),
                ('genre', models.CharField(blank=True, max_length=100, null=True)),
                ('publisher', models.CharField(blank=True, max_length=100, null=True)),
                ('record', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Catalogue.record')),
            ],
        ),
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(blank=True, max_length=100, null=True)),
                ('artist_lifespan', models.TextField(blank=True, null=True)),
                ('dimensions', models.CharField(blank=True, max_length=100, null=True)),
                ('supplies_used', models.CharField(blank=True, max_length=100, null=True)),
                ('art_style', models.TextField(blank=True, null=True)),
                ('record', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Catalogue.record')),
            ],
        ),
    ]
