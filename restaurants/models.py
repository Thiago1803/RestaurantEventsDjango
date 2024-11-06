from django.db import models
from django.contrib.auth.models import User


# null define se aceita ou não "valores nulos"
# blank define se aceita ou não "valores em branco"


# ------------------------------- CharField -------------------------------
# Define um campo VARCHAR no banco de dados
    # max_length define o tamanho maximo de uma string no banco


# ------------------------------- DateTimeField -------------------------------
# Define um campo DATETIME no banco de dados
    # auto_now_add pega a hora da criação do registro no banco


class Restaurants(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name="Restaurante")
    address = models.CharField(max_length=200, null=False, blank=False, verbose_name="Endereço")
    phone = models.CharField(max_length=15, null=True, blank=True, verbose_name="Telefone")
    email = models.CharField(max_length=100, null=True, blank=True, verbose_name="Email")
    opening_time = models.TimeField(null=False, blank=False, verbose_name="Abertura")
    closing_time = models.TimeField(null=False, blank=False, verbose_name="Fechamento")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    users = models.ManyToManyField(User, related_name="restaurants", verbose_name="Usuários")  # Relação para indicar quais usuários são administradores do restaurante


    # fiz essa parte abaixo pois o nome que estava aparecendo era o nome da tabela, ficando em ingles
    class Meta:
        verbose_name = "Restaurante"  # No ambiente admin, esse é o nome que irá aparecer nos lugares onde o nome no singular é usado
        verbose_name_plural = "Restaurantes"  # No ambiente admin, esse é o nome que irá aparecer nos lugares onde o nome no plural é usado


    # fiz essa parte abaixo pois o nome que estava aparecendo era o nome da tabela, ficando em ingles
    def __str__(self) -> str:
        return self.name
