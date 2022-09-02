# Generated by Django 3.1.14 on 2022-08-31 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autores',
            fields=[
                ('idAutor', models.BigAutoField(primary_key=True, serialize=False)),
                ('autor', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('idCategoria', models.BigAutoField(primary_key=True, serialize=False)),
                ('Categoria', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Editoriales',
            fields=[
                ('idEditorial', models.BigAutoField(primary_key=True, serialize=False)),
                ('Editorial', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Libros',
            fields=[
                ('idAsin', models.BigAutoField(primary_key=True, serialize=False)),
                ('Titulo', models.CharField(max_length=50)),
                ('Fecha_Lanzamiento', models.DateField()),
                ('Idioma', models.CharField(choices=[('Esp', 'Español'), ('Ing', 'Ingles'), ('Fra', 'Frances'), ('Ale', 'Aleman'), ('Chi', 'Chino')], default='ESP', max_length=3)),
                ('Paginas', models.IntegerField()),
                ('Descripcion', models.TextField()),
                ('Autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Biblioteca.autores')),
                ('Categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Biblioteca.categorias')),
                ('Editorial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Biblioteca.editoriales')),
            ],
        ),
    ]