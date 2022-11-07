# Generated by Django 3.2.15 on 2022-10-21 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selecao', '0007_auto_20221019_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidato',
            name='autodeclaracao',
            field=models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], max_length=1, verbose_name='O candidato é autodeclarado preto, pardo ou indígena'),
        ),
    ]