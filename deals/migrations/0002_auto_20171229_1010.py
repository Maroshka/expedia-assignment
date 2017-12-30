# Generated by Django 2.0 on 2017-12-29 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regionIds', models.IntegerField(blank=True, null=True)),
                ('minTripStartDate', models.DateField(blank=True, null=True)),
                ('maxTripStartDate', models.DateField(blank=True, null=True)),
                ('lengthOfStay', models.IntegerField(blank=True, null=True)),
                ('maxStarRating', models.IntegerField(blank=True, null=True)),
                ('minStarRating', models.IntegerField(blank=True, null=True)),
                ('maxTotalRate', models.IntegerField(blank=True, null=True)),
                ('minTotalRate', models.IntegerField(blank=True, null=True)),
                ('maxGuestRating', models.IntegerField(blank=True, null=True)),
                ('minGuestRating', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='SavedAttrs',
        ),
    ]