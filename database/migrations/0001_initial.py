# Generated by Django 3.2.7 on 2021-12-29 06:03

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=30)),
                ('subject', models.CharField(max_length=50)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('discription', models.TextField(max_length=200)),
                ('discount', models.FloatField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/upload_to')),
                ('trend', models.BooleanField(default=False)),
                ('off', models.IntegerField(default=0)),
                ('spacification', models.CharField(default='', max_length=200)),
                ('is_slider', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.category')),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.category')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('title', models.CharField(max_length=40)),
                ('review', models.TextField()),
                ('rating', models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5)])),
                ('createDate', models.DateField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=160)),
                ('verify', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='', upload_to='media')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductDiscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title1_image', models.ImageField(default='', upload_to='media')),
                ('title1_heading', models.CharField(max_length=200)),
                ('title1_discription', models.TextField()),
                ('title2_image', models.ImageField(default='', upload_to='media')),
                ('title2_heading', models.CharField(max_length=200)),
                ('title2_discription', models.TextField()),
                ('title3_image', models.ImageField(default='', upload_to='media')),
                ('title3_heading', models.CharField(max_length=200)),
                ('title3_discription', models.TextField()),
                ('title4_image', models.ImageField(default='', upload_to='media')),
                ('title4_heading', models.CharField(max_length=200)),
                ('title4_discription', models.TextField()),
                ('title5_image', models.ImageField(default='', upload_to='media')),
                ('title5_heading', models.CharField(max_length=200)),
                ('title5_discription', models.TextField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.subcategory'),
        ),
        migrations.CreateModel(
            name='AditionalInform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.CharField(max_length=300)),
                ('Weight_Dimensions', models.TextField()),
                ('display', models.TextField()),
                ('iSight_Camera', models.TextField()),
                ('VideoRecording', models.TextField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.product')),
            ],
        ),
    ]
