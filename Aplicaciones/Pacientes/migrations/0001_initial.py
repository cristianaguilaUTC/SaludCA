# Generated by Django 5.2 on 2025-05-13 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('cedula', models.CharField(max_length=15)),
                ('edad', models.CharField(max_length=100)),
                ('tipo_sangre', models.CharField(max_length=100)),
                ('seguro', models.CharField(max_length=100)),
                ('direccion', models.TextField()),
            ],
        ),
    ]
