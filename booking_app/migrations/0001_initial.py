from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('room_name', models.CharField(choices=[('1', 'Meeting Room 1'), ('2', 'Meeting Room 2'), ('3', 'Meeting Room 3')], max_length=1)),
                ('employee_id', models.IntegerField()),
                ('date_from', models.DateTimeField()),
                ('date_to', models.DateTimeField()),
            ],
        ),
    ]
