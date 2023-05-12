from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Delegacia

admin.site.site_header = "Delegacias Especializadas"


class DelegaciaAdmin(admin.ModelAdmin):
    list_display = ('cidade', 'crime', 'endereco', 'criacao', 'atualizacao', 'ativo')
    list_filter = ('cidade', 'crime')


admin.site.register(Delegacia, DelegaciaAdmin)
admin.site.unregister(Group)
