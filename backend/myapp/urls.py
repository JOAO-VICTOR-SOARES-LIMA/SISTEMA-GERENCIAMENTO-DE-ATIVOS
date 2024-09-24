from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CampoAdicionalViewSet, CampoAdicionalTabelaViewSet, CargoViewSet, DepartamentoViewSet, 
    DispositivoViewSet, EntidadeViewSet, EntidadeDispositivoViewSet, EntidadeLicencaViewSet, 
    LicencaViewSet, PerfilViewSet, PerfilDispositivoViewSet, SetorViewSet, 
    TelefoniaViewSet, TipoLicencaViewSet
)

# Criação do roteador
router = DefaultRouter()
router.register(r'campo-adicional', CampoAdicionalViewSet)
router.register(r'campo-adicional-tabela', CampoAdicionalTabelaViewSet)
router.register(r'cargo', CargoViewSet)
router.register(r'departamento', DepartamentoViewSet)
router.register(r'dispositivo', DispositivoViewSet)
router.register(r'entidade', EntidadeViewSet)
router.register(r'entidade-dispositivo', EntidadeDispositivoViewSet)
router.register(r'entidade-licenca', EntidadeLicencaViewSet)
router.register(r'licenca', LicencaViewSet)
router.register(r'perfil', PerfilViewSet)
router.register(r'perfil-dispositivo', PerfilDispositivoViewSet)
router.register(r'setor', SetorViewSet)
router.register(r'telefonia', TelefoniaViewSet)
router.register(r'tipo-licenca', TipoLicencaViewSet)

# Incluindo as rotas nas URLs
urlpatterns = [
    path('', include(router.urls)),
]