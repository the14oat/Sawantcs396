# Generated by Django 4.2.5 on 2023-10-06 06:15

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0003_postcomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='postBody',
            field=ckeditor.fields.RichTextField(),
        ),
    ]