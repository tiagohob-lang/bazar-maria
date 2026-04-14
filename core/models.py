from django.db import models

class Publico(models.Model):
    # Ex: Feminino, Masculino, Menina, Menino, Bebe
    nome = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Públicos"

    def __str__(self):
        return self.nome

class TipoRoupa(models.Model):
    # Ex: Blusas, Calças, Sapatos, Acessórios
    nome = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Tipos de Roupa"

    def __str__(self):
        return self.nome

class Produto(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Filtros robustos
    publico = models.ForeignKey(Publico, on_delete=models.PROTECT)
    tipo = models.ForeignKey(TipoRoupa, on_delete=models.PROTECT)
    
    imagem = models.ImageField(upload_to='produtos/', null=True, blank=True)
    estoque = models.IntegerField(default=1) # No bazar geralmente é 1
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} - {self.publico}"