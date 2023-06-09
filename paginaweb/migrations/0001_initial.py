# Generated by Django 3.1.7 on 2021-10-10 03:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=30)),
                ('nombre', models.CharField(max_length=30)),
                ('rut', models.IntegerField()),
                ('fecha_ingreso', models.DateField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'profesores',
            },
        ),
        migrations.CreateModel(
            name='Instrucciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clase', models.CharField(max_length=50)),
                ('horas', models.IntegerField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=8)),
                ('foto', models.ImageField(upload_to='img')),
                ('tipo', models.CharField(choices=[('combate', 'combate'), ('crossfit', 'crossfit'), ('pesas', 'pesas'), ('zumba', 'zumba')], default='crossfit', max_length=10)),
                ('profesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paginaweb.profesor')),
            ],
            options={
                'verbose_name_plural': 'Instrucciones',
            },
        ),
    ]
