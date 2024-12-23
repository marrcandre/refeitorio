# Generated by Django 5.1.2 on 2024-12-19 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_alter_user_email_alter_user_passage_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cardapio",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "dia",
                    models.CharField(
                        choices=[
                            ("SEG", "Segunda-feira"),
                            ("TER", "Terça-feira"),
                            ("QUA", "Quarta-feira"),
                            ("QUI", "Quinta-feira"),
                            ("SEX", "Sexta-feira"),
                        ],
                        max_length=3,
                        unique=True,
                    ),
                ),
                ("proteina", models.CharField(max_length=100)),
                ("opcao_vegetariana", models.CharField(max_length=100)),
                ("acompanhamento", models.TextField()),
                ("saladas", models.TextField()),
                ("sobremesa", models.CharField(max_length=100)),
            ],
        ),
    ]
