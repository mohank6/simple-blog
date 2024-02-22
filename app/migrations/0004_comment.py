# Generated by Django 5.0.2 on 2024-02-22 05:05

import app.utils.utils
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_post_is_deleted_alter_category_name_alter_post_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.CharField(db_index=True, default=app.utils.utils.get_char_uuid, editable=False, max_length=100, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('content', models.TextField()),
                ('is_approved', models.BooleanField(default=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='app.post')),
            ],
            options={
                'unique_together': {('post', 'email')},
            },
        ),
    ]
