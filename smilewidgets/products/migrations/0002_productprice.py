# Generated by Django 2.0.7 on 2019-05-02 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_type', models.CharField(help_text='pricing type', max_length=30)),
                ('price_start_date', models.DateField()),
                ('price_end_date', models.DateField(null=True)),
                ('product_price', models.PositiveIntegerField(help_text='Price in Cents')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
        ),
    ]
