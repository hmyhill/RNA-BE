# Generated by Django 4.2.7 on 2023-12-10 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("article", "0002_post_tags"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="post",
            options={},
        ),
        migrations.RemoveField(
            model_name="post",
            name="author",
        ),
        migrations.RemoveField(
            model_name="post",
            name="created_on",
        ),
        migrations.RemoveField(
            model_name="post",
            name="slug",
        ),
        migrations.RemoveField(
            model_name="post",
            name="status",
        ),
        migrations.RemoveField(
            model_name="post",
            name="tags",
        ),
        migrations.RemoveField(
            model_name="post",
            name="updated_on",
        ),
        migrations.AddField(
            model_name="post",
            name="category",
            field=models.IntegerField(
                choices=[
                    (0, "---"),
                    (1, "Entertainment"),
                    (2, "Sport"),
                    (3, "Technology"),
                    (4, "World"),
                ],
                default=0,
            ),
        ),
        migrations.AddField(
            model_name="post",
            name="imageURl",
            field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="post",
            name="content",
            field=models.TextField(default=""),
        ),
    ]
