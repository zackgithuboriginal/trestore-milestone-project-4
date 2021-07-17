# Generated by Django 3.2.3 on 2021-07-15 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_profiles', '0005_alter_userprofile_tree_planting_contribution'),
        ('blog', '0003_alter_progresspost_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_content', models.CharField(max_length=400)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comments', to='user_profiles.userprofile')),
                ('post', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.progresspost')),
            ],
        ),
    ]