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

class Tamanho(models.Model):
    nome = models.CharField(max_length=50, unique=True) # Ex: "P", "M", "42", "Único"

    class Meta:
        verbose_name_plural = "Tamanhos"

    def __str__(self):
        return self.nome

class Cor(models.Model):
    nome = models.CharField(max_length=30, unique=True) # Ex: "Preto", "Branco", "Azul", "Vermelho"
    codigo = models.CharField(max_length=7, default="#FFFFFF", help_text="Ex: #FF0000")

    class Meta:
        verbose_name_plural = "Cores"

    def __str__(self):
        return self.nome

class Produto(models.Model):
    CONDICAO_CHOICES = [
        ('N', 'Novo'),
        ('U', 'Usado'),
    ]

    ESTADO_CHOICES = [
        (1, 'Regular'),
        (2, 'Bom'),
        (3, 'Ótimo'),
        (4, 'Excelente'),
    ]    

    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    tamanho = models.ForeignKey('Tamanho', on_delete=models.SET_NULL, null=True, blank=True)
    condicao = models.CharField(max_length=1, choices=CONDICAO_CHOICES, default='U')
    estado = models.IntegerField(choices=ESTADO_CHOICES, default=2)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    publico = models.ForeignKey('Publico', on_delete=models.PROTECT)
    tipo = models.ForeignKey('TipoRoupa', on_delete=models.PROTECT)
    imagem = models.ImageField(upload_to='produtos/', null=True, blank=True)
    estoque = models.IntegerField(default=1) 
    material = models.CharField(max_length=100)
    medidas = models.TextField(blank=True, help_text="Ex: Busto 90cm, Comprimento 60cm")
    cor = models.ForeignKey('Cor', on_delete=models.SET_NULL, null=True, blank=True)
    em_destaque = models.BooleanField(default=False)
    vendido = models.BooleanField(default=False, verbose_name="Vendido?")
    criado_em = models.DateTimeField(auto_now_add=True)

    def gerar_sku(self):
        if not self.id:
            return "Pendente"
        return f"BM-{self.id:05d}"

    def __str__(self):
        # Usando o SKU no __str__ facilita muito a sua vida no Admin!
        return f"{self.gerar_sku()} - {self.titulo}"
    
class ImagemProduto(models.Model):
    produto = models.ForeignKey(Produto, related_name='imagens', on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='produtos/galeria/')

    class Meta:
        verbose_name = "Imagem do Produto"
        verbose_name_plural = "Galeria de Imagens"

    def __str__(self):
        return f"Foto de {self.produto.titulo}" 