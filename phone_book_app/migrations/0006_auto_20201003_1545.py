# Generated by Django 3.1.2 on 2020-10-03 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('phone_book_app', '0005_auto_20201003_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telefon',
            name='osoba',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='phone_book_app.osoba'),
        ),
    ]
