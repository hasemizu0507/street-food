# Generated by Django 2.2.1 on 2021-08-29 02:38

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
            name='Food',
            fields=[
                ('id', models.CharField(max_length=6, primary_key=True, serialize=False, verbose_name='商品ID')),
                ('food_name', models.CharField(max_length=20, verbose_name='商品名')),
                ('price', models.FloatField(verbose_name='価格')),
                ('image', models.CharField(max_length=20, verbose_name='画像ファイル')),
            ],
            options={
                'verbose_name': '商品データ',
                'verbose_name_plural': '商品データ',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('age', models.IntegerField(verbose_name='年齢')),
                ('gender', models.IntegerField(choices=[(0, '男性'), (1, '女性')], verbose_name='性別')),
                ('pref_name', models.CharField(max_length=20, verbose_name='都道府県')),
                ('city_name', models.CharField(max_length=50, verbose_name='市区町村')),
                ('district_name', models.CharField(max_length=50, verbose_name='町丁目')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ユーザー')),
            ],
            options={
                'verbose_name': 'ユーザー情報データ',
                'verbose_name_plural': 'ユーザー情報データ',
            },
        ),
    ]
