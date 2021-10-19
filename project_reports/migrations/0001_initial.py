# Generated by Django 2.2.8 on 2021-09-22 22:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import picklefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectReportFromEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email_prefix', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Project report reminder email address',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='ProjectReportBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('presidents_letter', models.TextField()),
                ('pdf', models.FileField(blank=True, upload_to='project_report_books/')),
                ('exception', picklefield.fields.PickledObjectField(editable=False, null=True)),
                ('terms', models.ManyToManyField(to='base.Term')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('title', models.CharField(max_length=80)),
                ('area', models.CharField(blank=True, choices=[('cl', 'Community/Liberal Culture'), ('uc', 'University/College'), ('pe', 'Profession/Engineering'), ('cs', 'Chapter/Social'), ('ep', 'Education/Prof. Dev.'), ('km', 'K-12/MindSET')], max_length=2)),
                ('organize_hours', models.PositiveSmallIntegerField(default=0, help_text='Number of hours spent organizing the event.')),
                ('participate_hours', models.PositiveSmallIntegerField(default=0, help_text='Number of hours spent by a single person participating in the event.')),
                ('is_new', models.BooleanField(default=False, help_text='Was this the first time an event like this had been held?')),
                ('other_group', models.CharField(blank=True, help_text='Name(s) of any other organization that also participated and/or helped organize the event.', max_length=60)),
                ('description', models.TextField(help_text='General description of event, vendors, sponsors, etc. Use markdown formatting.')),
                ('purpose', models.TextField()),
                ('organization', models.TextField(help_text='Setup, number of people involved, clean-up, etc.')),
                ('cost', models.TextField()),
                ('problems', models.TextField()),
                ('results', models.TextField()),
                ('non_tbp', models.PositiveSmallIntegerField(default=0, help_text='Number of non-TBP participants')),
                ('complete', models.BooleanField(default=False, help_text='Is this project report finished?')),
                ('first_completed_at', models.DateTimeField(blank=True, null=True)),
                ('attachment', models.FileField(blank=True, upload_to='pr')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('candidate_list', models.ManyToManyField(blank=True, related_name='_projectreport_candidate_list_+', to=settings.AUTH_USER_MODEL)),
                ('committee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.OfficerPosition')),
                ('member_list', models.ManyToManyField(blank=True, related_name='_projectreport_member_list_+', to=settings.AUTH_USER_MODEL)),
                ('officer_list', models.ManyToManyField(blank=True, related_name='_projectreport_officer_list_+', to=settings.AUTH_USER_MODEL)),
                ('term', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.Term')),
            ],
            options={
                'ordering': ('date',),
                'permissions': (('view_project_reports', 'Can view all project reports'),),
            },
        ),
    ]
