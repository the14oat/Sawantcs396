# Generated by Django 4.2.5 on 2023-10-06 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0006_exercise_multiplechoice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='multiplechoice',
            old_name='question',
            new_name='questionName',
        ),
    ]