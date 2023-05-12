from django.db import models


class Base(models.Model):
    criacao = models.DateTimeField(auto_created=True)
    atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Delegacia(Base):
    cidade = models.CharField(max_length=255)
    crime = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)


    class Meta:
        verbose_name = 'delegacia'
        verbose_name_plural = 'delegacias'

    def __str__(self):
        return self.cidade