# Generated by Django 2.2.1 on 2021-08-29 08:15

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
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=6)),
                ('product_id', models.CharField(max_length=6)),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='追加日時')),
                ('pref_name', models.CharField(max_length=20, verbose_name='都道府県')),
                ('city_name', models.CharField(max_length=50, verbose_name='市区町村')),
                ('district_name', models.CharField(max_length=50, verbose_name='町丁目')),
            ],
            options={
                'verbose_name': 'カート情報',
                'verbose_name_plural': 'カート情報',
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
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.CharField(max_length=6, primary_key=True, serialize=False, verbose_name='商品ID')),
                ('food_name', models.CharField(max_length=20, verbose_name='商品名')),
                ('price', models.FloatField(verbose_name='価格')),
                ('image', models.CharField(max_length=20, verbose_name='画像ファイル')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='streetfood.Profile', verbose_name='所有者')),
            ],
            options={
                'verbose_name': '商品データ',
                'verbose_name_plural': '商品データ',
            },
        ),
    ]
