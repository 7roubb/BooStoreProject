# Generated by Django 4.2.11 on 2024-06-06 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('author', models.CharField(blank=True, max_length=100, null=True)),
                ('price', models.CharField(max_length=100, null=True)),
                ('issuDate', models.DateField(blank=True, null=True)),
                ('category', models.CharField(choices=[('Fiction', 'Fiction'), ('Non-Fiction', 'Non-Fiction'), ('Biography', 'Biography'), ('Thriller', 'Thriller'), ('Romance', 'Romance'), ('Horror', 'Horror'), ('Mystery', 'Mystery'), ('Sci-Fi', 'Sci-Fi'), ('Self-Help', 'Self-Help'), ('Health', 'Health'), ('Cooking', 'Cooking'), ('History', 'History'), ('Travel', 'Travel'), ('Education', 'Education'), ('Business', 'Business'), ('Politics', 'Politics'), ('Religion', 'Religion'), ('Spirituality', 'Spirituality'), ('Science', 'Science'), ('Technology', 'Technology')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('status', models.CharField(choices=[('IN ORDER', 'IN ORDER'), ('DELIVERED', 'DELIVERED'), ('CANCELLED', 'CANCELLED'), ('RETURNED', 'RETURNED'), ('PENDING', 'PENDING'), ('DELIVERING', 'DELIVERING')], max_length=100)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Store.book')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Store.customer')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='tag',
            field=models.ManyToManyField(blank=True, null=True, to='Store.tag'),
        ),
    ]
