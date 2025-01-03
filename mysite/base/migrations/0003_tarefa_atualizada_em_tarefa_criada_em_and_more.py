# Generated by Django 5.1.4 on 2025-01-02 00:27

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_tarefa'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarefa',
            name='atualizada_em',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='tarefa',
            name='criada_em',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tarefa',
            name='nome',
            field=models.CharField(max_length=255),
        ),
    ]
