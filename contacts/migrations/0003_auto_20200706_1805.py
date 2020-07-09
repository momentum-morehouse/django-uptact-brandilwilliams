from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '002_contact_birthday'),  
     ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
    ] 