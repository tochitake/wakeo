# Generated by Django 2.1.5 on 2019-10-16 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, verbose_name='コメント')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='メンバー名')),
                ('div', models.CharField(blank=True, max_length=255, verbose_name='所属')),
                ('sex', models.CharField(blank=True, max_length=255, verbose_name='性別')),
                ('team', models.IntegerField(blank=True, default=0, verbose_name='チーム')),
                ('serialcd', models.CharField(blank=True, max_length=255, verbose_name='シリアルコード')),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='ページ名')),
                ('serialcd', models.CharField(max_length=255, verbose_name='シリアルコード')),
                ('memo', models.CharField(blank=True, max_length=255, verbose_name='メモ')),
            ],
        ),
        migrations.AddField(
            model_name='attribute',
            name='rel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attributes', to='cms.Member', verbose_name=''),
        ),
    ]
