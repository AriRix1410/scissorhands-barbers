# Generated by Django 3.2.14 on 2022-07-28 18:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('booking', '0002_auto_20220728_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barber',
            name='barbername',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='barber',
            name='service',
            field=models.CharField(choices=[('Gents Cut', 'Gents Cut'), ('Kids Cut', 'Kids Cut'), ('Cut and Shave', 'Cut and Shave'), ('Shave Only', 'Shave Only')], max_length=50, null=True),
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('barber', models.CharField(blank=True, max_length=50, null=True)),
                ('service', models.CharField(blank=True, max_length=50, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
