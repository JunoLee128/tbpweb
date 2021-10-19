# Generated by Django 2.2.8 on 2021-09-22 22:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of the company.', max_length=255, unique=True)),
                ('website', models.URLField(blank=True, help_text='The company website.', max_length=255)),
                ('logo', models.ImageField(blank=True, help_text='The company logo.', upload_to='company_logos/')),
                ('expiration_date', models.DateField(help_text='The date the company account subscription expires.')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'companies',
                'permissions': (('view_companies', 'Can view information about companies'),),
            },
        ),
        migrations.CreateModel(
            name='CompanyRep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.ForeignKey(help_text='The Company this contact is associated with.', on_delete=django.db.models.deletion.CASCADE, to='companies.Company')),
                ('user', models.OneToOneField(help_text='The user account for this company contact', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('view_companyreps', 'Can view information about company reps'),),
            },
        ),
    ]
