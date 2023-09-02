from django.db import models


class User(models.Model):
    STATUS_CHOICES = (("ACTIVE", "Ativo"), ("INACTIVE", "Inativo"))

    ## Basic info
    username = models.CharField(max_length=255)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    cpf = models.CharField(max_length=11, blank=True, null=True)
    status = models.CharField(
        max_length=20, blank=True, null=True, choices=STATUS_CHOICES
    )
    created_at = models.DateTimeField("Created at", auto_now_add=True)
    updated_at = models.DateTimeField("Updated at", auto_now=True)

    ## Address
    cep = models.CharField(max_length=8, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    complement = models.CharField(max_length=300, blank=True, null=True)
    neighborhood = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)

    ## Contacts
    cellphone = models.CharField(max_length=100, blank=True, null=True)
    telephone = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    linkedin = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["created_at"]
