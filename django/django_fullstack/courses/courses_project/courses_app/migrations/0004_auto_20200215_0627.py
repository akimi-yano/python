# Generated by Django 2.2 on 2020-02-15 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses_app', '0003_auto_20200215_0609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='description',
            name='course',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='courses_app.Course'),
        ),
    ]
