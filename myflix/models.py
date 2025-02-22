from django.db import models

class user(models.Model):
    nome = models.CharField(max_length = 100)
    email = models.EmailField(blank=False, max_length=30)
    cpf = models.CharField(max_length = 11)
    data_nascimento = models.DateField()
    celular = models.CharField(max_length = 14)

    def __str__(self):
        return self.nome

class stream(models.Model):
    CATEGORIA = (
        ('F', 'Filme'),
        ('S', 'Série'),
        ('D', 'Documentário')
    )
    codigo = models.CharField(max_length = 10)
    descricao = models.CharField(max_length = 100, blank=False)
    categoria = models.CharField(max_length=1, choices=CATEGORIA, blank=False, default='F')

    def __str__(self):
        return self.codigo

class lista(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    stream = models.ForeignKey(stream, on_delete=models.CASCADE)