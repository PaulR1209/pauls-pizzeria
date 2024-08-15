from django.db import migrations, models
import datetime

def copy_date_data(apps, schema_editor):
    BookingAssignment = apps.get_model('booking', 'BookingAssignment')
    for assignment in BookingAssignment.objects.all():
        # Assuming the old date field was a timestamp (bigint)
        assignment.temp_date = datetime.date.fromtimestamp(assignment.date)
        assignment.save()

def copy_time_data(apps, schema_editor):
    BookingAssignment = apps.get_model('booking', 'BookingAssignment')
    for assignment in BookingAssignment.objects.all():
        # Assuming the old time field was a timestamp (bigint)
        assignment.temp_time = datetime.time.fromtimestamp(assignment.time)
        assignment.save()

class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_bookingassignment'),  # Replace with your actual previous migration file
    ]

    operations = [
        migrations.AddField(
            model_name='bookingassignment',
            name='temp_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='bookingassignment',
            name='temp_time',
            field=models.TimeField(null=True),
        ),
        migrations.RunPython(copy_date_data),
        migrations.RunPython(copy_time_data),
        migrations.RemoveField(
            model_name='bookingassignment',
            name='date',
        ),
        migrations.RemoveField(
            model_name='bookingassignment',
            name='time',
        ),
        migrations.RenameField(
            model_name='bookingassignment',
            old_name='temp_date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='bookingassignment',
            old_name='temp_time',
            new_name='time',
        ),
        migrations.AlterField(
            model_name='bookingassignment',
            name='guests',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='bookingassignment',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]