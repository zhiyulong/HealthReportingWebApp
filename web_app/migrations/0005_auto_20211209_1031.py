# Generated by Django 2.1.15 on 2021-12-09 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0004_auto_20211209_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recordedquestion',
            name='healthRecord',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='web_app.HealthRecord'),
        ),
    ]