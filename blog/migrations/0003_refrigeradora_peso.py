# Generated by Django 4.1.3 on 2022-11-30 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_refrigheradora_refrigeradora'),
    ]

    operations = [
        migrations.AddField(
            model_name='refrigeradora',
            name='peso',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
