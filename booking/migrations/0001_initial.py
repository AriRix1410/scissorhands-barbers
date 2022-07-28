# Generated by Django 3.2.14 on 2022-07-28 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Barber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('service', models.CharField(choices=[('Gents Cut', 'Gents Cut'), ('Kids Cut', 'Kids Cut'), ('Cut and Shave', 'Cut and Shave'), ('Shave Only', 'Shave Only')], max_length=100, null=True)),
            ],
        ),
    ]
