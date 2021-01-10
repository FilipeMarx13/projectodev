from django.db import models

# Create your models here.

class cadastro_pessoa(models.Model):
    nome = models.CharField(max_length=16, null=False, verbose_name="Nome")
    sobrenome = models.CharField(max_length=32, null=False, verbose_name="Sobrenome")
    idade = models.PositiveIntegerField()
    data_nascimento = models.DateField(null=False, verbose_name="Data de Nascimento")
    email = models.EmailField(null=False, verbose_name="E-mail", unique=True)
    apelido = models.CharField(max_length=8, verbose_name="Apelido") #preciso colocar blank=true e null=true
    observacao = models.TextField(blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Cadastro_Pessoas"

    def get_data_nascimento(self):
        return self.data_nascimento.strftime('%d/%m/%Y')

    #def __str__(self):
       #return self.id
