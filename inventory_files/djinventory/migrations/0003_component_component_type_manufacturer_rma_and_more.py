# Generated by Django 4.1.3 on 2022-11-09 01:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djinventory', '0002_system_system_update_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Serial_number', models.CharField(max_length=100, unique=True)),
                ('Label', models.CharField(blank=True, max_length=100, null=True)),
                ('Manual_assignment', models.BooleanField(default=False)),
                ('Account', models.CharField(blank=True, max_length=100, null=True)),
                ('Added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Component_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Information', models.TextField(blank=True, null=True)),
                ('Added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Return_address_street', models.CharField(max_length=2000)),
                ('Return_address_city_state_zip', models.CharField(max_length=2000)),
                ('Documentation', models.TextField()),
                ('Owner', models.CharField(max_length=15)),
                ('Added', models.DateTimeField(auto_now_add=True)),
                ('Shipped_to_vendor', models.BooleanField(default=False)),
                ('Returned_from_vendor', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Rma_reasons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Reason', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Rma_status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Status', models.CharField(max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Vendor_name', models.CharField(max_length=50)),
                ('Vendor_link', models.CharField(max_length=200)),
                ('Notes', models.TextField()),
                ('Added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rma_pictures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Picture', models.ImageField(upload_to='rmas')),
                ('Notes', models.CharField(max_length=1000)),
                ('Rma', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='djinventory.rma')),
            ],
        ),
        migrations.AddField(
            model_name='rma',
            name='Reason',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='djinventory.rma_reasons'),
        ),
        migrations.AddField(
            model_name='rma',
            name='Status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='djinventory.rma_status'),
        ),
        migrations.AddField(
            model_name='rma',
            name='Vendor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='djinventory.vendor'),
        ),
        migrations.CreateModel(
            name='Component_log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Account', models.CharField(blank=True, max_length=100, null=True)),
                ('Added', models.DateTimeField(auto_now_add=True)),
                ('Component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djinventory.component')),
                ('New_system', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='djinventory.system')),
                ('Old_system', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='djinventory.system')),
            ],
        ),
        migrations.CreateModel(
            name='Component_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Part_number', models.CharField(max_length=100, unique=True)),
                ('Capacity', models.CharField(blank=True, max_length=10, null=True)),
                ('Capacity_type', models.CharField(blank=True, choices=[('KB', 'KB'), ('GB', 'GB'), ('MB', 'MB'), ('TB', 'TB')], max_length=2)),
                ('Added', models.DateTimeField(auto_now_add=True)),
                ('Component_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djinventory.component_type')),
                ('Manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djinventory.manufacturer')),
            ],
        ),
        migrations.AddField(
            model_name='component',
            name='Part_number',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='djinventory.component_list'),
        ),
        migrations.AddField(
            model_name='component',
            name='Rma',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='djinventory.rma'),
        ),
        migrations.AddField(
            model_name='component',
            name='System',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='djinventory.system'),
        ),
    ]
