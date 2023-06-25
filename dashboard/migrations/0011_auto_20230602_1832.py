# Generated by Django 3.2 on 2023-06-02 23:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_carrera_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.DecimalField(decimal_places=2, max_digits=4)),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.alumno')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.curso')),
            ],
        ),
        migrations.RemoveField(
            model_name='notalaboratorio',
            name='curso',
        ),
        migrations.DeleteModel(
            name='Horario',
        ),
        migrations.DeleteModel(
            name='NotaLaboratorio',
        ),
    ]
