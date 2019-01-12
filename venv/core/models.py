from django.db import models
import math

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Marca(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Veiculo(models.Model):
    nome = models.CharField(max_length=25)
    marca = models.ForeignKey(Marca)
    proprietario = models.ForeignKey(Pessoa)
    placa = models.CharField(max_length=8)
    cor = models.CharField(max_length=15)
    observacao = models.TextField(blank=True)

    def __str__(self):
        return self.nome + ' - ' + self.placa

class Parametros(models.Model):
    valor_hora = models.DecimalField(max_digits=5, decimal_places=2)
    valor_mes = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return "Parâmetros Gerais."

class MovRotativo(models.Model):
    checkIn = models.DateTimeField(auto_now=False)
    checkOut = models.DateTimeField(auto_now=False, blank=True, null=True)
    valor_hora = models.DecimalField(max_digits=5, decimal_places=2)
    veiculo = models.ForeignKey(Veiculo)
    pago = models.BooleanField(default=False)

    def horas_total(self):
        return math.ceil((self.checkOut - self.checkIn).total_seconds() / 3600)

    def total(self):
        return self.valor_hora * self.horas_total()
    
    def __str__(self):
        return self.veiculo.placa

class Mensalista(models.Model):
    veiculo = models.ForeignKey(Veiculo)
    inicio = models.DateField()
    valor_mes = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return str(self.veiculo) + ' - ' + str(self.inicio)

class MovMensalista(models.Model):
    mensalista = models.ForeignKey(Mensalista)
    dt_pgto = models.DateField()
    total = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return str(self.mensalista)
    
    def total_dias(self):
        dif = self.dt_pgto - self.mensalista.inicio
        return dif.days
    
    def total_pgto(self):
        return self.total_dias() * round(self.mensalista.valor_mes / 30, 2)

