# Generated by Django 5.1.6 on 2025-02-14 05:21

import taggit.managers
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='photo',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='date',
            new_name='published_date',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='summury',
            new_name='summary',
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
