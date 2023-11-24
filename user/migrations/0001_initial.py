# Generated by Django 4.2.7 on 2023-11-24 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('address_street', models.CharField(blank=True, max_length=100, null=True)),
                ('address_city', models.CharField(blank=True, max_length=50, null=True)),
                ('address_state', models.CharField(blank=True, max_length=50, null=True)),
                ('address_zip', models.CharField(blank=True, max_length=10, null=True)),
                ('user_type', models.CharField(choices=[('Parent', 'Parent'), ('Child', 'Child')], max_length=10)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]
