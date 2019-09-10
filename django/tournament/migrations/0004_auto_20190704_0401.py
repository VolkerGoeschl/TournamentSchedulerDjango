# Generated by Django 2.2.1 on 2019-07-04 04:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0003_auto_20190703_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='away_score',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='home_score',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='referee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='referee_matches', to='tournament.TeamPlaceholder'),
        ),
    ]