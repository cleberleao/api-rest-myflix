# Generated by Django 5.1.6 on 2025-02-22 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myflix', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='stream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10)),
                ('descricao', models.CharField(max_length=100)),
                ('categoria', models.CharField(choices=[('F', 'Filme'), ('S', 'Série'), ('D', 'Documentário')], default='F', max_length=1)),
            ],
        ),
    ]
