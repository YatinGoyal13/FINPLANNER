# Generated by Django 4.2.2 on 2023-08-11 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("investment", "0004_invest_pdf_file_invest_uploaded_at_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="FundsOffer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("type", models.CharField(max_length=50)),
                ("description", models.CharField(max_length=200)),
                ("category", models.IntegerField()),
            ],
        ),
    ]