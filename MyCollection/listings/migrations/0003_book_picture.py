# Generated by Django 4.2.1 on 2023-06-20 13:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Listings", "0002_book_author"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="picture",
            field=models.ImageField(null=True, upload_to="book_pictures/"),
        ),
    ]
