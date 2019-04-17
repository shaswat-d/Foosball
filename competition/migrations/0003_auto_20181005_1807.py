# Generated by Django 2.1.2 on 2018-10-05 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0002_auto_20181005_1757'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='points',
            new_name='foosball_points',
        ),
        migrations.AddField(
            model_name='match',
            name='game',
            field=models.CharField(choices=[('TT', 'TT'), ('FS', 'foosball')], default=None, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='tt_points',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
