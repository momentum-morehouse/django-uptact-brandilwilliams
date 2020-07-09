from django.db import migration, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_contact_note'),
    ]
    
    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='note',
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.Charfield(blank=True, max_length=255, null=True))
                ('date_added', models.DateTimeField (auto_now_add=True)),
                ('contact', models.ForeignKey (on_delete=django.db.models.deletion.CASCADE, to='contacts.Contact')),
            ],
        ),
    ]
