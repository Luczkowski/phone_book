# Generated by Django 3.1.2 on 2020-10-03 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('phone_book_app', '0002_auto_20201002_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='osoba',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='phone_book_app.osoba'),
        ),
        migrations.AlterField(
            model_name='telefon',
            name='osoba',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='phone_book_app.osoba'),
        ),
    ]
