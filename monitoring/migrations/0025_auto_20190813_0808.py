# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-08-13 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0024_auto_20190605_1619'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('OWS:TMS','TMS'), ('OWS:WMS-C','WMS-C'), ('OWS:WMTS','WMTS'), ('OWS:WCS','WCS'), ('OWS:WFS','WFS'), ('OWS:WMS','WMS'), ('OWS:WPS','WPS'), ('other','Non-OWS'), ('OWS:ALL','Any OWS'), ('all','All'), ('create','Create'), ('upload','Upload'), ('change','Change'), ('change_metadata','Change Metadata'), ('view_metadata','View Metadata'), ('view','View'), ('download','Download'), ('publish','Publish'), ('remove','Remove'), ('geoserver','Geoserver event')], max_length=16, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='metricnotificationcheck',
            name='ows_service',
        ),
        migrations.RemoveField(
            model_name='notificationmetricdefinition',
            name='use_ows_service',
        ),
        migrations.RemoveField(
            model_name='requestevent',
            name='ows_service',
        ),
        migrations.AddField(
            model_name='notificationmetricdefinition',
            name='use_event_type',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='requestevent',
            name='user_anonymous',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='requestevent',
            name='user_identifier',
            field=models.CharField(blank=True, db_index=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='monitoredresource',
            name='type',
            field=models.CharField(choices=[('','No resource'), ('layer','Layer'), ('map','Map'), ('resource base','Resource base'), ('document','Document'), ('style','Style'), ('admin','Admin'), ('url','URL'), ('other','Other')], default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='requestevent',
            name='client_ip',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='metricnotificationcheck',
            name='event_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='monitoring.EventType'),
        ),
        migrations.AddField(
            model_name='metricvalue',
            name='event_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='metric_values', to='monitoring.EventType'),
        ),
        migrations.AddField(
            model_name='requestevent',
            name='event_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='monitoring.EventType'),
        ),
        migrations.AlterUniqueTogether(
            name='metricvalue',
            unique_together=set(
                [('valid_from', 'valid_to', 'service', 'service_metric', 'resource', 'label', 'event_type')]),
        ),
        migrations.RemoveField(
            model_name='metricvalue',
            name='ows_service',
        ),
        migrations.DeleteModel(
            name='OWSService',
        ),
    ]