# Generated by Django 3.1.7 on 2021-05-19 23:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agricultura',
            options={},
        ),
        migrations.AddField(
            model_name='agricultura',
            name='topado_por',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='myapp.topado'),
        ),
        migrations.AddField(
            model_name='construccion',
            name='topado_por',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='myapp.topado'),
        ),
        migrations.AddField(
            model_name='coronas',
            name='topado_por',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='myapp.topado'),
        ),
        migrations.AddField(
            model_name='flores',
            name='topado_por',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='myapp.topado'),
        ),
        migrations.AddField(
            model_name='transporte',
            name='topado_por',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='myapp.topado'),
        ),
        migrations.AlterUniqueTogether(
            name='agricultura',
            unique_together={('producto', 'topado_por')},
        ),
        migrations.AlterUniqueTogether(
            name='construccion',
            unique_together={('producto', 'topado_por')},
        ),
        migrations.AlterUniqueTogether(
            name='coronas',
            unique_together={('variedades_de_flores', 'topado_por')},
        ),
        migrations.AlterUniqueTogether(
            name='flores',
            unique_together={('descripcion', 'topado_por')},
        ),
    ]
