from dJngo.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '002_auto_20200706_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='note',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]