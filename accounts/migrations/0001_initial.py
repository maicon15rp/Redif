# Generated by Django 4.0.2 on 2022-07-11 20:43

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('titulacao', models.CharField(choices=[('1', 'Fundamental 2 ao 8°ano'), ('2', 'Cursando 9° ano'), ('3', 'Cursando Ensino Médio'), ('4', 'Ensino Médio Completo'), ('5', 'Ensino Médio Incompleto'), ('6', 'Cursando Ensino Superior'), ('7', 'Ensino Superior Completo')], max_length=1)),
                ('tipo', models.CharField(choices=[('P', 'Professor'), ('A', 'Aluno')], max_length=1)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
