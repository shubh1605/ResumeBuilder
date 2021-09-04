# Generated by Django 3.1.7 on 2021-09-04 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_basicinformation_profession'),
    ]

    operations = [
        migrations.RenameField(
            model_name='education',
            old_name='stream',
            new_name='branch',
        ),
        migrations.RemoveField(
            model_name='experience',
            name='city',
        ),
        migrations.RemoveField(
            model_name='experience',
            name='state',
        ),
        migrations.AddField(
            model_name='education',
            name='university',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='education',
            name='degree',
            field=models.CharField(choices=[('Phd', 'Phd'), ('Mtech/MA/MSc/MCom/MBA', 'Masters'), ('BE/Btech/BA/BSc/BCom', 'Bachlors'), ('12th', 'High School'), ('10th', 'School')], max_length=50),
        ),
    ]