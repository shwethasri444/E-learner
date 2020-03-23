# Generated by Django 2.1.2 on 2020-02-27 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('elearnerapp', '0003_auto_20200227_1333'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionanswer',
            name='question',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='text',
            new_name='q_text',
        ),
        migrations.RenameField(
            model_name='questionnaire',
            old_name='version',
            new_name='topic',
        ),
        migrations.AddField(
            model_name='question',
            name='correct',
            field=models.CharField(default='E', max_length=5),
        ),
        migrations.AddField(
            model_name='question',
            name='option_a',
            field=models.CharField(default='default', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='option_b',
            field=models.CharField(default='default', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='option_c',
            field=models.CharField(default='default', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='option_d',
            field=models.CharField(default='default', max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='useranswer',
            name='answer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elearnerapp.Question'),
        ),
        migrations.DeleteModel(
            name='QuestionAnswer',
        ),
    ]