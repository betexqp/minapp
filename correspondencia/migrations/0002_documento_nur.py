# Generated by Django 3.2.16 on 2022-10-07 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('correspondencia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='nur',
            field=models.CharField(choices=[('externo', 'E-MDPyEP'), ('interno', 'MDPyEP')], default='externo', max_length=10),
        ),
    ]
