# Generated by Django 4.0.1 on 2022-01-20 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_delete_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='etudiant',
            name='classe',
        ),
        migrations.RemoveField(
            model_name='matiere',
            name='module',
        ),
        migrations.RemoveField(
            model_name='module',
            name='classe',
        ),
        migrations.RemoveField(
            model_name='note',
            name='etudiant',
        ),
        migrations.RemoveField(
            model_name='note',
            name='matiere',
        ),
        migrations.RemoveField(
            model_name='specialite',
            name='classe',
        ),
        migrations.DeleteModel(
            name='classe',
        ),
        migrations.DeleteModel(
            name='etudiant',
        ),
        migrations.DeleteModel(
            name='matiere',
        ),
        migrations.DeleteModel(
            name='module',
        ),
        migrations.DeleteModel(
            name='note',
        ),
        migrations.DeleteModel(
            name='specialite',
        ),
    ]