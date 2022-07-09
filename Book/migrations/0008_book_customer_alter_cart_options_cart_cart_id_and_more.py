# Generated by Django 4.0.5 on 2022-07-09 17:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Book', '0007_books_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('year_published', models.CharField(max_length=4)),
                ('publisher', models.CharField(max_length=200)),
                ('category', models.CharField(blank=True, max_length=255, null=True)),
                ('price', models.FloatField(default=0)),
                ('description', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterModelOptions(
            name='cart',
            options={'ordering': ['cart_id', 'created_at']},
        ),
        migrations.AddField(
            model_name='cart',
            name='cart_id',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cart',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.CreateModel(
            name='Burgain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('your_price', models.FloatField(default=0)),
                ('is_approved', models.BooleanField(default=False)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Book.book')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Book.customer')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]