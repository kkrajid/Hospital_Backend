# Generated by Django 4.2.5 on 2023-12-13 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_appointment_amount_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='amount_paid',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
