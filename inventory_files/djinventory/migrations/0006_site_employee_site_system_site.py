# Generated by Django 4.1.3 on 2022-11-09 02:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djinventory', '0005_purchase'),
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Site_name', models.CharField(max_length=200)),
                ('Street', models.CharField(max_length=32)),
                ('City', models.CharField(max_length=32)),
                ('State', models.CharField(default='TX', max_length=2)),
                ('Country', models.CharField(default='USA', max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='Site',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='djinventory.site'),
        ),
        migrations.AddField(
            model_name='system',
            name='Site',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='djinventory.site'),
        ),
    ]