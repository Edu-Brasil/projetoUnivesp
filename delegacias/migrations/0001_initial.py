# Generated by Django 4.2.1 on 2023-05-10 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Delegacia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criacao', models.DateTimeField(auto_created=True)),
                ('atualizacao', models.DateTimeField(auto_now=True)),
                ('ativo', models.BooleanField(default=True)),
                ('cidade', models.CharField(max_length=255)),
                ('crime', models.CharField(max_length=255)),
                ('endereco', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'delegacia',
                'verbose_name_plural': 'delegacias',
            },
        ),
    ]