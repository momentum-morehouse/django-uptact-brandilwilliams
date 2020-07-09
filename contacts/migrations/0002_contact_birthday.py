from django.db import migrations, models

class Migration (migrations.Migration):

    dependencies =[ 
        ('contacts',    '001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='birthday',
            field=models.Charfield (blank=True, max_length=40, null=True),
        ),
    ]