# Generated by Django 4.2.16 on 2024-10-24 13:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="news",
            options={
                "ordering": ["-created_at", "-title"],
                "verbose_name": "Новость",
                "verbose_name_plural": "Новости",
            },
        ),
        migrations.AlterField(
            model_name="news",
            name="content",
            field=models.TextField(blank=True, verbose_name="Контекст"),
        ),
        migrations.AlterField(
            model_name="news",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, verbose_name="Дата публикации"
            ),
        ),
        migrations.AlterField(
            model_name="news",
            name="is_published",
            field=models.BooleanField(default=True, verbose_name="Опубликовано"),
        ),
        migrations.AlterField(
            model_name="news",
            name="photo",
            field=models.ImageField(
                blank=True, upload_to="photos/%Y/%m/%d/", verbose_name="Фото"
            ),
        ),
        migrations.AlterField(
            model_name="news",
            name="title",
            field=models.CharField(max_length=150, verbose_name="Наименование"),
        ),
        migrations.AlterField(
            model_name="news",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, verbose_name="Дата обновления"),
        ),
    ]
