from django.db import models

#Esta classe pode conter informações sobre o casal, como nomes, data do casamento, biografias e fotos.

class CasalDeNoivos(models.Model):
    nome_do_noivo = models.CharField(max_length=100)
    nome_da_noiva = models.CharField(max_length=100)
    data_do_casamento = models.DateField()
    biografia_do_noivo = models.TextField()
    biografia_da_noiva = models.TextField()
    foto_do_noivo = models.ImageField(upload_to='fotos/')
    foto_da_noiva = models.ImageField(upload_to='fotos/')


def __str__(self):
    return f"Casamento de {self.nome_noivo} e {self.nome_noiva}"

#Esta classe pode conter informações sobre o local do casamento, como nome, endereço e descrição

class LocalDoEvento(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.TextField()
    descricao = models.TextField()

#Esta classe pode conter informações sobre os convidados, como nome, e-mail e confirmação de presença.

class Convidado(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    confirmado = models.BooleanField(default=False)

#Esta classe pode conter informações sobre os presentes desejados pelo casal.

class Presente(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    link = models.URLField()
